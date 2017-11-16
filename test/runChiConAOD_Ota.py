#This example can be run over files from AOD, therefore we need to build some information in fly.
#
outFileName = 'Run285549eventsLoose.root'
#inFileNames = 'file:aod-input.root'

inFileNames = 'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/0249A3C5-A2B1-E611-8E3E-FA163ED701FA.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/02D119C2-A2B1-E611-ABC6-FA163E5F661C.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/063FF92E-C6B1-E611-A5B4-02163E014625.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/06D275D0-B5B1-E611-AB0A-02163E011D75.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/08654C12-B8B1-E611-A9A1-02163E012010.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/0A538293-CFB1-E611-A842-FA163E3004A8.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/14C2AAE7-A2B1-E611-8D3E-02163E011A12.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/18B36ED4-A2B1-E611-BB2A-02163E011BD3.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/1A141540-BAB1-E611-8F2E-02163E0134FC.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/1C08CBE0-B8B1-E611-9E4D-FA163ECE0FC7.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/1C2479E1-A2B1-E611-8840-02163E0124A3.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/1C2E39EB-C9B1-E611-A027-FA163EEB149D.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/1E562DCC-A2B1-E611-B9BC-02163E0144FB.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/2269FA31-C2B1-E611-8BB6-02163E01433B.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/2277EFF7-B7B1-E611-BF79-FA163E6BAB6E.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/28B25D6B-C7B1-E611-907F-02163E012B6A.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/2A02D9DB-A2B1-E611-A027-02163E0118D2.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/2C889CCC-A2B1-E611-9433-02163E014303.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/2CC8D63E-BBB1-E611-9F77-02163E014453.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/2CE4AEB3-A2B1-E611-871A-FA163E966790.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/2E97B7B9-A2B1-E611-9252-02163E011CA0.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/302532B9-A2B1-E611-A353-02163E0141C6.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/305003BD-A2B1-E611-94DA-FA163E245FA9.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/345FAD97-BAB1-E611-895B-02163E0136C3.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/347634C6-A2B1-E611-823D-02163E014156.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/3A7EC61E-C3B1-E611-BDF0-02163E0133E8.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/3E0C8BCF-A2B1-E611-968A-02163E011D2E.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/3E2B60FD-B7B1-E611-ACDB-02163E0141C6.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/40B0BDE8-B5B1-E611-A0EB-FA163E7111D0.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/425F2004-C3B1-E611-903E-FA163EEAF06B.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/463443B5-A2B1-E611-B00F-FA163EA53949.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/469751B7-A2B1-E611-9AEA-02163E01341F.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/4AB3CFD3-C4B1-E611-98A5-FA163ED8DBB5.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/4EAE1BB9-C6B1-E611-BF0C-02163E013396.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/5208FFBE-A2B1-E611-8EC1-FA163E18AC85.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/526BEEE2-B8B1-E611-9AF8-FA163E6A249C.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/58441C06-A2B1-E611-8851-02163E011BFA.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/58AD59BE-A2B1-E611-B895-FA163EA2631E.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/5AE2D6C8-A2B1-E611-A689-02163E01359A.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/5E656418-C1B1-E611-9E53-FA163E604650.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/60F59325-C5B1-E611-A645-02163E0133BA.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/66A2A85D-B6B1-E611-AA37-02163E01184F.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/6A2874F0-D2B1-E611-84AA-FA163EBF8C40.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/705837F3-B8B1-E611-88D4-02163E014474.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/722255C5-A2B1-E611-911C-02163E01414A.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/72BB8EC5-A2B1-E611-9A5B-02163E01417D.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/74EB5CBB-A2B1-E611-907B-FA163EBF6D58.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/762301F6-C5B1-E611-8B9B-02163E014459.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/7821A6BF-C5B1-E611-BEBF-02163E0137FB.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/7AC845AF-C4B1-E611-AA8D-02163E0146B1.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/7AE33FB7-A2B1-E611-A283-02163E013942.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/7C05A1BE-A2B1-E611-8F7D-FA163EFFABD1.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/7CA759C8-BBB1-E611-9CE9-02163E0144D1.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/7E9027C4-A2B1-E611-B012-FA163E6DC769.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/823E52BF-A2B1-E611-835B-02163E014672.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/82540487-C7B1-E611-8BB5-FA163EEA92CC.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/88C021A8-B7B1-E611-A067-02163E012292.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/8A4DB6C6-A2B1-E611-A27F-02163E013914.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/8A7CDBB7-C6B1-E611-B84C-FA163E177A6B.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/8C4ABFB9-C5B1-E611-BB88-02163E011DDA.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/90A4EB07-A2B1-E611-9431-FA163E01ADA3.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/921E2CFE-BCB1-E611-A2F2-02163E011E45.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/92C4A917-C6B1-E611-A644-FA163EAA51C4.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/960D3CBB-A2B1-E611-90B7-FA163E82AA7E.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/960EF8DA-A2B1-E611-ABCB-02163E012154.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/96D52708-A2B1-E611-A4EF-02163E011C63.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/9A3C75F5-A1B1-E611-979B-FA163EA4A793.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/9AFAFB11-B9B1-E611-82EE-FA163E6CFF59.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/9C4D9562-B6B1-E611-8158-02163E0126F4.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/9E361FC0-A2B1-E611-B9FC-02163E01415B.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/9E51AE64-BDB1-E611-8333-02163E014708.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/A02190C1-A2B1-E611-8ABC-02163E014751.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/A0671AC9-A2B1-E611-898B-02163E014728.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/A216B94D-A1B1-E611-A087-02163E01352F.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/A22EF2B9-A2B1-E611-B652-FA163E72A280.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/A46AA1C2-A2B1-E611-BEC6-02163E0145C0.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/A60258DB-A2B1-E611-B720-02163E012B45.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/A6BA120D-CCB1-E611-885C-FA163E95C5A3.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/A80FBAB8-B3B1-E611-8357-FA163E6A249C.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/A83C9921-BCB1-E611-9FF8-02163E0143E8.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/AAB2C208-A2B1-E611-9B0A-02163E011878.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/B02364CC-A2B1-E611-9AE2-02163E013627.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/B6A1D440-C6B1-E611-9FA9-02163E0141F3.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/B88037DF-A2B1-E611-9984-02163E0139DA.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/BA5EAAC3-A2B1-E611-8D8C-FA163E3496C7.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/BC2EB399-C4B1-E611-8966-FA163E921868.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/BC95A9BD-A2B1-E611-A423-02163E01415C.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/BEEE32C5-A2B1-E611-87A2-02163E0135C1.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/C0281A02-A2B1-E611-AAB5-02163E01422D.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/C21D49C2-A2B1-E611-AB09-FA163E84683B.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/C292A1D6-A2B1-E611-B01D-02163E012A84.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/C2A57966-C8B1-E611-BC44-02163E01338F.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/C8A97AD1-A2B1-E611-A71F-02163E0118B7.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/CA00C57D-A3B1-E611-B9CD-02163E0142FA.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/CA0F38BE-C2B1-E611-9CE2-02163E0119B1.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/CA551750-B6B1-E611-BB84-FA163E59CC31.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/CA77FE97-BAB1-E611-A017-02163E012145.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/CCB3599D-C6B1-E611-A3C5-02163E014704.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/CE9CDDED-BBB1-E611-A90C-FA163E358FEB.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/D05EE3B5-A2B1-E611-B476-FA163ED6CCEE.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/D46D4FD7-B6B1-E611-A635-02163E0134FF.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/D6FFBEFC-A1B1-E611-8832-02163E0142D0.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/D8114BD9-A2B1-E611-9843-02163E011993.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/D8D205C2-A2B1-E611-BC57-02163E0142E6.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/DAC1C79D-CDB1-E611-AB7E-FA163E36269D.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/DC3596D2-B8B1-E611-A12C-02163E01438D.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/E44E97CB-A2B1-E611-84FC-02163E014105.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/E4624244-BBB1-E611-851F-02163E0119B1.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/EA11F80B-A2B1-E611-A838-FA163EE96F44.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/EAF51BBD-A2B1-E611-9514-02163E01466E.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/EC9D1EE3-CAB1-E611-A406-FA163EECE5C8.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/ECAB57CE-A2B1-E611-B01E-02163E014215.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/EE08B7FC-A1B1-E611-A780-02163E0142D0.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/EE5B9AC7-B9B1-E611-9B61-FA163EAA51C4.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/F83229E7-C5B1-E611-9074-FA163ED6CCEE.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/FA6C07D9-BEB1-E611-A98E-02163E01466B.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/FAF2F3C3-A2B1-E611-A396-02163E0144AE.root'

import FWCore.ParameterSet.Config as cms
import FWCore.PythonUtilities.LumiList as LumiList

process = cms.Process("Rootuple")

process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.Reconstruction_cff')

process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_data', '')

process.GlobalTag.toGet = cms.VPSet(
  cms.PSet(
    record = cms.string("HeavyIonRcd"),
    tag = cms.string("CentralityTable_HFtowersPlusTrunc200_EPOS8TeV_v80x01_mc"),
    connect = cms.string("frontier://FrontierProd/CMS_CONDITIONS"),
    label = cms.untracked.string("HFtowersPlusTruncEpos")
    )
  )

process.MessageLogger.cerr.FwkReport.reportEvery = 1000
process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))

#process.source = cms.Source("PoolSource",fileNames = cms.untracked.vstring('file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/0249A3C5-A2B1-E611-8E3E-FA163ED701FA.root',
#'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/02D119C2-A2B1-E611-ABC6-FA163E5F661C.root',
##'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/063FF92E-C6B1-E611-A5B4-02163E014625.root',
##'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/06D275D0-B5B1-E611-AB0A-02163E011D75.root',
##'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/08654C12-B8B1-E611-A9A1-02163E012010.root',
##'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/0A538293-CFB1-E611-A842-FA163E3004A8.root',
##'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/EE5B9AC7-B9B1-E611-9B61-FA163EAA51C4.root',
##'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/F83229E7-C5B1-E611-9074-FA163ED6CCEE.root',
##'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/FA6C07D9-BEB1-E611-A98E-02163E01466B.root',
#'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/FAF2F3C3-A2B1-E611-A396-02163E0144AE.root'))

process.source = cms.Source("PoolSource",fileNames = cms.untracked.vstring('file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/0249A3C5-A2B1-E611-8E3E-FA163ED701FA.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/02D119C2-A2B1-E611-ABC6-FA163E5F661C.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/063FF92E-C6B1-E611-A5B4-02163E014625.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/06D275D0-B5B1-E611-AB0A-02163E011D75.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/08654C12-B8B1-E611-A9A1-02163E012010.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/0A538293-CFB1-E611-A842-FA163E3004A8.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/14C2AAE7-A2B1-E611-8D3E-02163E011A12.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/18B36ED4-A2B1-E611-BB2A-02163E011BD3.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/1A141540-BAB1-E611-8F2E-02163E0134FC.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/1C08CBE0-B8B1-E611-9E4D-FA163ECE0FC7.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/1C2479E1-A2B1-E611-8840-02163E0124A3.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/1C2E39EB-C9B1-E611-A027-FA163EEB149D.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/1E562DCC-A2B1-E611-B9BC-02163E0144FB.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/2269FA31-C2B1-E611-8BB6-02163E01433B.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/2277EFF7-B7B1-E611-BF79-FA163E6BAB6E.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/28B25D6B-C7B1-E611-907F-02163E012B6A.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/2A02D9DB-A2B1-E611-A027-02163E0118D2.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/2C889CCC-A2B1-E611-9433-02163E014303.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/2CC8D63E-BBB1-E611-9F77-02163E014453.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/2CE4AEB3-A2B1-E611-871A-FA163E966790.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/2E97B7B9-A2B1-E611-9252-02163E011CA0.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/302532B9-A2B1-E611-A353-02163E0141C6.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/305003BD-A2B1-E611-94DA-FA163E245FA9.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/345FAD97-BAB1-E611-895B-02163E0136C3.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/347634C6-A2B1-E611-823D-02163E014156.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/3A7EC61E-C3B1-E611-BDF0-02163E0133E8.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/3E0C8BCF-A2B1-E611-968A-02163E011D2E.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/3E2B60FD-B7B1-E611-ACDB-02163E0141C6.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/40B0BDE8-B5B1-E611-A0EB-FA163E7111D0.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/425F2004-C3B1-E611-903E-FA163EEAF06B.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/463443B5-A2B1-E611-B00F-FA163EA53949.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/469751B7-A2B1-E611-9AEA-02163E01341F.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/4AB3CFD3-C4B1-E611-98A5-FA163ED8DBB5.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/4EAE1BB9-C6B1-E611-BF0C-02163E013396.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/5208FFBE-A2B1-E611-8EC1-FA163E18AC85.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/526BEEE2-B8B1-E611-9AF8-FA163E6A249C.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/58441C06-A2B1-E611-8851-02163E011BFA.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/58AD59BE-A2B1-E611-B895-FA163EA2631E.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/5AE2D6C8-A2B1-E611-A689-02163E01359A.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/5E656418-C1B1-E611-9E53-FA163E604650.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/60F59325-C5B1-E611-A645-02163E0133BA.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/66A2A85D-B6B1-E611-AA37-02163E01184F.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/6A2874F0-D2B1-E611-84AA-FA163EBF8C40.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/705837F3-B8B1-E611-88D4-02163E014474.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/722255C5-A2B1-E611-911C-02163E01414A.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/72BB8EC5-A2B1-E611-9A5B-02163E01417D.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/74EB5CBB-A2B1-E611-907B-FA163EBF6D58.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/762301F6-C5B1-E611-8B9B-02163E014459.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/7821A6BF-C5B1-E611-BEBF-02163E0137FB.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/7AC845AF-C4B1-E611-AA8D-02163E0146B1.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/7AE33FB7-A2B1-E611-A283-02163E013942.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/7C05A1BE-A2B1-E611-8F7D-FA163EFFABD1.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/7CA759C8-BBB1-E611-9CE9-02163E0144D1.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/7E9027C4-A2B1-E611-B012-FA163E6DC769.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/823E52BF-A2B1-E611-835B-02163E014672.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/82540487-C7B1-E611-8BB5-FA163EEA92CC.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/88C021A8-B7B1-E611-A067-02163E012292.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/8A4DB6C6-A2B1-E611-A27F-02163E013914.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/8A7CDBB7-C6B1-E611-B84C-FA163E177A6B.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/8C4ABFB9-C5B1-E611-BB88-02163E011DDA.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/90A4EB07-A2B1-E611-9431-FA163E01ADA3.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/921E2CFE-BCB1-E611-A2F2-02163E011E45.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/92C4A917-C6B1-E611-A644-FA163EAA51C4.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/960D3CBB-A2B1-E611-90B7-FA163E82AA7E.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/960EF8DA-A2B1-E611-ABCB-02163E012154.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/96D52708-A2B1-E611-A4EF-02163E011C63.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/9A3C75F5-A1B1-E611-979B-FA163EA4A793.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/9AFAFB11-B9B1-E611-82EE-FA163E6CFF59.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/9C4D9562-B6B1-E611-8158-02163E0126F4.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/9E361FC0-A2B1-E611-B9FC-02163E01415B.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/9E51AE64-BDB1-E611-8333-02163E014708.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/A02190C1-A2B1-E611-8ABC-02163E014751.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/A0671AC9-A2B1-E611-898B-02163E014728.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/A216B94D-A1B1-E611-A087-02163E01352F.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/A22EF2B9-A2B1-E611-B652-FA163E72A280.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/A46AA1C2-A2B1-E611-BEC6-02163E0145C0.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/A60258DB-A2B1-E611-B720-02163E012B45.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/A6BA120D-CCB1-E611-885C-FA163E95C5A3.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/A80FBAB8-B3B1-E611-8357-FA163E6A249C.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/A83C9921-BCB1-E611-9FF8-02163E0143E8.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/AAB2C208-A2B1-E611-9B0A-02163E011878.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/B02364CC-A2B1-E611-9AE2-02163E013627.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/B6A1D440-C6B1-E611-9FA9-02163E0141F3.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/B88037DF-A2B1-E611-9984-02163E0139DA.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/BA5EAAC3-A2B1-E611-8D8C-FA163E3496C7.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/BC2EB399-C4B1-E611-8966-FA163E921868.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/BC95A9BD-A2B1-E611-A423-02163E01415C.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/BEEE32C5-A2B1-E611-87A2-02163E0135C1.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/C0281A02-A2B1-E611-AAB5-02163E01422D.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/C21D49C2-A2B1-E611-AB09-FA163E84683B.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/C292A1D6-A2B1-E611-B01D-02163E012A84.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/C2A57966-C8B1-E611-BC44-02163E01338F.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/C8A97AD1-A2B1-E611-A71F-02163E0118B7.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/CA00C57D-A3B1-E611-B9CD-02163E0142FA.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/CA0F38BE-C2B1-E611-9CE2-02163E0119B1.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/CA551750-B6B1-E611-BB84-FA163E59CC31.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/CA77FE97-BAB1-E611-A017-02163E012145.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/CCB3599D-C6B1-E611-A3C5-02163E014704.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/CE9CDDED-BBB1-E611-A90C-FA163E358FEB.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/D05EE3B5-A2B1-E611-B476-FA163ED6CCEE.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/D46D4FD7-B6B1-E611-A635-02163E0134FF.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/D6FFBEFC-A1B1-E611-8832-02163E0142D0.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/D8114BD9-A2B1-E611-9843-02163E011993.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/D8D205C2-A2B1-E611-BC57-02163E0142E6.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/DAC1C79D-CDB1-E611-AB7E-FA163E36269D.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/DC3596D2-B8B1-E611-A12C-02163E01438D.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/E44E97CB-A2B1-E611-84FC-02163E014105.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/E4624244-BBB1-E611-851F-02163E0119B1.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/EA11F80B-A2B1-E611-A838-FA163EE96F44.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/EAF51BBD-A2B1-E611-9514-02163E01466E.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/EC9D1EE3-CAB1-E611-A406-FA163EECE5C8.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/ECAB57CE-A2B1-E611-B01E-02163E014215.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/EE08B7FC-A1B1-E611-A780-02163E0142D0.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/EE5B9AC7-B9B1-E611-9B61-FA163EAA51C4.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/F83229E7-C5B1-E611-9074-FA163ED6CCEE.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/FA6C07D9-BEB1-E611-A98E-02163E01466B.root',
'file:/eos/cms/store/hidata/PARun2016C/PADoubleMuon/AOD/PromptReco-v1/000/285/549/00000/FAF2F3C3-A2B1-E611-A396-02163E0144AE.root'))

#process.source = cms.Source("PoolSource",fileNames = cms.untracked.vstring('file:/afs/cern.ch/user/o/okukral/Chi_pPb/CMSSW_8_0_24_patch1/src/Ponia/OniaPhoton/test/EventOta3.root'))
#process.source.lumisToProcess = LumiList.LumiList(filename = 'Run285549.json').getVLuminosityBlockRange()
process.TFileService = cms.Service("TFileService",fileName = cms.string(outFileName))
process.options   = cms.untracked.PSet( wantSummary = cms.untracked.bool(False))

# muons without trigger info, alternatively in recent version of 80x you can use muon with trigger as well.
# we will select muons and create Onia2MuMu pairs.
import PhysicsTools.PatAlgos.producersLayer1.muonProducer_cfi
process.oniaPATMuonsWithoutTrigger = PhysicsTools.PatAlgos.producersLayer1.muonProducer_cfi.patMuons.clone(
    muonSource = 'muons',
    embedTrack          = True,
    embedCombinedMuon   = True,
    embedStandAloneMuon = True,
    embedPFCandidate    = False,
    embedCaloMETMuonCorrs = cms.bool(False),
    embedTcMETMuonCorrs   = cms.bool(False),
    embedPfEcalEnergy     = cms.bool(False),
    embedPickyMuon = False,
    embedTpfmsMuon = False,
    userIsolation = cms.PSet(),   # no extra isolation beyond what's in reco::Muon itself
    isoDeposits = cms.PSet(),     # no heavy isodeposits
    addGenMatch = False,          # no mc
)

process.oniaSelectedMuons = cms.EDFilter('PATMuonSelector',
   src = cms.InputTag('oniaPATMuonsWithoutTrigger'),
   cut = cms.string('muonID(\"TMOneStationTight\")'
                   # ' && abs(innerTrack.dxy) < 0.3'
                   # ' && abs(innerTrack.dz)  < 20.'
                    ' && innerTrack.hitPattern.trackerLayersWithMeasurement > 5'
                    ' && innerTrack.hitPattern.pixelLayersWithMeasurement > 0'
                    ' && innerTrack.quality(\"highPurity\")'
                    ' && ((abs(eta) <= 0.9 && pt > 2.5) || (0.9 < abs(eta) <= 2.4 && pt > 1.5))'
   ),
   filter = cms.bool(True)
)

process.load("HeavyFlavorAnalysis.Onia2MuMu.onia2MuMuPAT_cfi")
process.onia2MuMuPAT.muons=cms.InputTag('oniaSelectedMuons')
process.onia2MuMuPAT.primaryVertexTag=cms.InputTag('offlinePrimaryVertices')
process.onia2MuMuPAT.higherPuritySelection = cms.string("isGlobalMuon") #O
process.onia2MuMuPAT.lowerPuritySelection = cms.string("isTrackerMuon") #O
process.onia2MuMuPAT.beamSpotTag=cms.InputTag('offlineBeamSpot')
process.onia2MuMuPAT.dimuonSelection=cms.string("0.2 < mass && abs(daughter('muon1').innerTrack.dz - daughter('muon2').innerTrack.dz) < 25")
process.onia2MuMuPAT.addMCTruth = cms.bool(False)

# make photon candidate conversions for P-wave studies.
# The low energy photons are reconstructed here.
import HeavyFlavorAnalysis.Onia2MuMu.OniaPhotonConversionProducer_cfi
process.oniaPhotonCandidates = HeavyFlavorAnalysis.Onia2MuMu.OniaPhotonConversionProducer_cfi.PhotonCandidates.clone(
    conversions = 'allConversions',
    convAlgo    = 'undefined',
    convQuality = [''], #O: Changed ['highPurity','generalTracksOnly']
    primaryVertexTag = 'offlinePrimaryVertices',
    convSelection = 'conversionVertex.position.rho>0.0', #O: Changed 1.5
    wantTkVtxCompatibility = False,
    sigmaTkVtxComp = 50, #O: Changed 5
    wantCompatibleInnerHits = True,
    pfcandidates = 'particleFlow',
    pi0OnlineSwitch = False,
    TkMinNumOfDOF = 0, #O: Changed 3
    wantHighpurity = False,
    #test
    vertexChi2ProbCut = 0.0000,
    trackchi2Cut = 1000,
    minDistanceOfApproachMinCut = -100.25,
    minDistanceOfApproachMaxCut = 100.00,
    #O: Original
    #vertexChi2ProbCut = 0.0005,
    #trackchi2Cut = 10,
    #minDistanceOfApproachMinCut = -0.25,
    #minDistanceOfApproachMaxCut = 1.00,
)

# Centrality and other
# process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
# from Configuration.AlCa.GlobalTag import GlobalTag
# process.GlobalTag = GlobalTag(process.GlobalTag, '75X_mcRun2_HeavyIon_v10', '')

process.load("RecoHI.HiCentralityAlgos.CentralityBin_cfi")
process.centralityBin.Centrality = cms.InputTag("pACentrality")
process.centralityBin.centralityVariable = cms.string("HFtowersPlusTrunc")
process.centralityBin.nonDefaultGlauberModel = cms.string("Epos")

# with all pieces at hand, we procced in the standard way.
process.load('Ponia.OniaPhoton.OniaPhotonProducer_cfi')
process.load('Ponia.OniaPhoton.OniaPhotonRootupler_cfi')

tag_dimuon="onia2MuMuPAT"
tag_chi_conv_prod="oniaPhotonCandidates"
tag_chi_conv_lab="conversions"
process.DiMuonCounter.src = cms.InputTag(tag_dimuon)
process.PhotonCounter.src  = cms.InputTag(tag_chi_conv_prod,tag_chi_conv_lab)
process.ChiProducer.conversions = cms.InputTag(tag_chi_conv_prod, tag_chi_conv_lab)

process.p = cms.Path(
            process.oniaPATMuonsWithoutTrigger *
            process.oniaSelectedMuons *
            process.onia2MuMuPAT *
            process.centralityBin *
            process.oniaPhotonCandidates *
            process.ChiSequence*process.rootuple
)
process.rootuple.isMC = cms.bool(False)