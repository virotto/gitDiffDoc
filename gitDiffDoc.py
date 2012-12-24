#!/usr/bin/python
#-*- coding: utf-8 -*-

import commands
import cgi

class DiffInfo:
	def __init__(self):
		self.oldFile = ""
		self.newFile = ""
		self.alteration = ""

xmlOutput = ''
xmlText1 = '<?xml version="1.0"?><?mso-application progid="Excel.Sheet"?><Workbook xmlns="urn:schemas-microsoft-com:office:spreadsheet" xmlns:o="urn:schemas-microsoft-com:office:office" xmlns:x="urn:schemas-microsoft-com:office:excel" xmlns:ss="urn:schemas-microsoft-com:office:spreadsheet" xmlns:html="http://www.w3.org/TR/REC-html40"> <DocumentProperties xmlns="urn:schemas-microsoft-com:office:office">  <Created>2006-09-13T11:12:02Z</Created>  <LastSaved>2012-12-23T18:12:49Z</LastSaved>  <Version>12.00</Version> </DocumentProperties> <OfficeDocumentSettings xmlns="urn:schemas-microsoft-com:office:office">  <RemovePersonalInformation/> </OfficeDocumentSettings> <ExcelWorkbook xmlns="urn:schemas-microsoft-com:office:excel">  <WindowHeight>12090</WindowHeight>  <WindowWidth>19200</WindowWidth>  <WindowTopX>0</WindowTopX>  <WindowTopY>30</WindowTopY>  <ProtectStructure>False</ProtectStructure>  <ProtectWindows>False</ProtectWindows> </ExcelWorkbook> <Styles>  <Style ss:ID="Default" ss:Name="Normal">   <Alignment ss:Vertical="Center"/>   <Borders/>   <Font ss:FontName="ＭＳ Ｐゴシック" x:CharSet="128" x:Family="Modern" ss:Size="11"    ss:Color="#000000"/>   <Interior/>   <NumberFormat/>   <Protection/>  </Style>  <Style ss:ID="s16">   <Font ss:FontName="ＭＳ Ｐゴシック" x:CharSet="128" x:Family="Modern" ss:Size="18"    ss:Color="#FFFFFF"/>  </Style>  <Style ss:ID="s17">   <Borders>    <Border ss:Position="Bottom" ss:LineStyle="Continuous" ss:Weight="1"/>    <Border ss:Position="Left" ss:LineStyle="Continuous" ss:Weight="1"/>    <Border ss:Position="Right" ss:LineStyle="Continuous" ss:Weight="1"/>    <Border ss:Position="Top" ss:LineStyle="Continuous" ss:Weight="1"/>   </Borders>   <Interior ss:Color="#C5D9F1" ss:Pattern="Solid"/>  </Style>  <Style ss:ID="s18">  <Alignment ss:Vertical="Center" ss:WrapText="1"/> <Borders>    <Border ss:Position="Bottom" ss:LineStyle="Continuous" ss:Weight="1"/>    <Border ss:Position="Left" ss:LineStyle="Continuous" ss:Weight="1"/>    <Border ss:Position="Right" ss:LineStyle="Continuous" ss:Weight="1"/>    <Border ss:Position="Top" ss:LineStyle="Continuous" ss:Weight="1"/>   </Borders>  </Style> </Styles> <Worksheet ss:Name="変更点記入書">  <Table ss:ExpandedColumnCount="4" x:FullColumns="1"   x:FullRows="1" ss:DefaultColumnWidth="54" ss:DefaultRowHeight="13.5">   <Column ss:AutoFitWidth="0" ss:Width="32.25"/>   <Column ss:AutoFitWidth="0" ss:Width="161.25"/>   <Column ss:AutoFitWidth="0" ss:Width="340.5"/>   <Column ss:AutoFitWidth="0" ss:Width="622.5"/>   <Row ss:Index="2" ss:AutoFitHeight="0" ss:Height="26.25">    <Cell ss:Index="2" ss:StyleID="s16"><PhoneticText      xmlns="urn:schemas-microsoft-com:office:excel">ヘンコウテンキニュウショ</PhoneticText><Data      ss:Type="String">変更点記入書</Data></Cell>   </Row>   <Row ss:Index="4">    <Cell ss:Index="2" ss:StyleID="s17"><PhoneticText      xmlns="urn:schemas-microsoft-com:office:excel">ツイカメイ</PhoneticText><Data      ss:Type="String">追加ファイル名</Data></Cell>    <Cell ss:StyleID="s17"><PhoneticText      xmlns="urn:schemas-microsoft-com:office:excel">ツイカリユウ</PhoneticText><Data      ss:Type="String">追加理由</Data></Cell>    <Cell ss:StyleID="s17"><PhoneticText      xmlns="urn:schemas-microsoft-com:office:excel">ナイヨウショウサイ</PhoneticText><Data      ss:Type="String">内容詳細</Data></Cell>   </Row>'
xmlText2 = '<Cell ss:Index="2" ss:StyleID="s17"><PhoneticText      xmlns="urn:schemas-microsoft-com:office:excel">サクジョメイ</PhoneticText><Data      ss:Type="String">削除ファイル名</Data></Cell>    <Cell ss:StyleID="s17"><PhoneticText      xmlns="urn:schemas-microsoft-com:office:excel">サクジョリユウ</PhoneticText><Data      ss:Type="String">削除理由</Data></Cell>    <Cell ss:StyleID="s17"><PhoneticText      xmlns="urn:schemas-microsoft-com:office:excel">ナイヨウショウサイ</PhoneticText><Data      ss:Type="String">内容詳細</Data></Cell>   </Row>'
xmlText3 = '<Cell ss:Index="2" ss:StyleID="s17"><PhoneticText      xmlns="urn:schemas-microsoft-com:office:excel">ヘンコウメイ</PhoneticText><Data      ss:Type="String">変更ファイル名</Data></Cell>    <Cell ss:StyleID="s17"><PhoneticText      xmlns="urn:schemas-microsoft-com:office:excel">ヘンコウリユウ</PhoneticText><Data      ss:Type="String">変更理由</Data></Cell>    <Cell ss:StyleID="s17"><PhoneticText      xmlns="urn:schemas-microsoft-com:office:excel">ナイヨウショウサイ</PhoneticText><Data      ss:Type="String">内容詳細</Data></Cell>   </Row>'
xmlText4 = '  </Table>  <WorksheetOptions xmlns="urn:schemas-microsoft-com:office:excel">   <PageSetup>    <Header x:Margin="0.3"/>    <Footer x:Margin="0.3"/>    <PageMargins x:Bottom="0.75" x:Left="0.7" x:Right="0.7" x:Top="0.75"/>   </PageSetup>   <Print>    <ValidPrinterInfo/>    <PaperSizeIndex>9</PaperSizeIndex>    <HorizontalResolution>300</HorizontalResolution>    <VerticalResolution>300</VerticalResolution>   </Print>   <Selected/>   <LeftColumnVisible>3</LeftColumnVisible>   <Panes>    <Pane>     <Number>3</Number>     <ActiveRow>5</ActiveRow>     <ActiveCol>3</ActiveCol>    </Pane>   </Panes>   <ProtectObjects>False</ProtectObjects>   <ProtectScenarios>False</ProtectScenarios>  </WorksheetOptions>  <ConditionalFormatting xmlns="urn:schemas-microsoft-com:office:excel">   <Range>R2</Range>   <Condition>    <Value1>ROW()=2</Value1>    <Format Style=\'background:#538ED5\'/>   </Condition>  </ConditionalFormatting> </Worksheet></Workbook>'

commands.getoutput('mkdir ./gitDiffDoc')
commands.getoutput('mkdir ./gitDiffDoc/after')
commands.getoutput('mkdir ./gitDiffDoc/before')

output = commands.getoutput('git diff HEAD').split('\n')

diffInfos = []
tmp = None

#get Infos(git diff parser)
for elem in output:
	if elem.startswith('diff'):
		if tmp != None:
			diffInfos.append(tmp)
		tmp = DiffInfo()
	elif elem.startswith('---'):
		tmp.oldFile = '.' + elem[5:]
	elif elem.startswith('+++'):
		tmp.newFile = '.' + elem[5:]
	elif elem.startswith('-'):
		tmp.alteration += elem + '&#10;'	
	elif elem.startswith('+'):
		tmp.alteration += elem + '&#10;'
diffInfos.append(tmp)

#make diff file (after and before)
#make after
for info in diffInfos:
	if info.newFile != ".dev/null":
		commands.getoutput('cp --parents ' + info.newFile + ' ./gitDiffDoc/after')
#copy after to before(to make folder)
commands.getoutput('cp -rf ./gitDiffDoc/after/* ./gitDiffDoc/before/')
#make before
for info in diffInfos:
	if info.newFile != ".dev/null":
		commands.getoutput('git show HEAD:' + info.newFile[2:] + ' > ./gitDiffDoc/before/' + info.newFile)
	if info.oldFile == ".dev/null":
		commands.getoutput('rm ./gitDiffDoc/before/' + info.newFile)
		
#make document(./gitDiffDoc/document.xml)
#add file
xmlOutput += xmlText1
count = 0
for info in diffInfos:
	if info.oldFile == ".dev/null":
		
		xmlOutput += '   <Row>    <Cell ss:Index="2" ss:StyleID="s18"><Data ss:Type="String">' + cgi.escape(info.newFile) + '</Data></Cell>    <Cell ss:StyleID="s18"><Data ss:Type="String"></Data></Cell>    <Cell ss:StyleID="s18"><Data ss:Type="String">' + '' +'</Data></Cell>   </Row>'
		count += 1
		

#delete file
xmlOutput += '<Row ss:Index="' + str(6+count) + '">'
xmlOutput += xmlText2
for info in diffInfos:
	if info.newFile == ".dev/null":
		xmlOutput += '   <Row>    <Cell ss:Index="2" ss:StyleID="s18"><Data ss:Type="String">' + cgi.escape(info.oldFile) + '</Data></Cell>    <Cell ss:StyleID="s18"><Data ss:Type="String"></Data></Cell>    <Cell ss:StyleID="s18"><Data ss:Type="String">' + '' +'</Data></Cell>   </Row>'
		count += 1

#modify file
xmlOutput += '<Row ss:Index="' + str(8+count) + '">'
xmlOutput += xmlText3
for info in diffInfos:
	if info.oldFile != ".dev/null" and info.newFile != ".dev/null":
		xmlOutput += '   <Row>    <Cell ss:Index="2" ss:StyleID="s18"><Data ss:Type="String">' + cgi.escape(info.newFile) + '</Data></Cell>    <Cell ss:StyleID="s18"><Data ss:Type="String"></Data></Cell>    <Cell ss:StyleID="s18"><Data ss:Type="String">' + '' +'</Data></Cell>   </Row>'
		count += 1
		

xmlOutput += xmlText4

#print xmlOutput
fp = open('./gitDiffDoc/document.xml','w')
fp.write(xmlOutput)
fp.close()
	
