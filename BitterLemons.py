#loop through Bitter Lemons Corpus and identify viewpoint
import os,re

#Working directory variable
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

folder = os.path.join(__location__, 'Corpora', 'BitterLemons', 'docs')

Israel =[]
Palestine = []

#Regex
IS = re.compile(r'is')
PAL = re.compile(r'pal')
for file in os.listdir(folder):
	IS = re.search( r'is', file, re.I)
	if IS:
		Israel.append(file)
	PAL = re.search(r'pal', file, re.I)
	if PAL:
		Palestine.append(file)

print "****** Israel******"
print Israel
print len(Israel)

print "****** Palestine ******"
print Palestine
print len(Palestine)

"""****** Israel******
['bl010304ed8is1', 'bl010304ed8is2', 'bl010702ed24is1', 'bl010702ed24is2', 'bl010903ed33is1', 'bl010903ed33is2', 'bl011104ed39is1', 'bl011104ed39is2', 'bl011203ed43is1', 'bl011203ed43is2', 'bl020603ed21is1', 'bl020603ed21is2', 'bl020804ed28is1', 'bl020804ed28is2', 'bl020902ed33is1', 'bl020902ed33is2', 'bl021202ed44is1', 'bl021202ed44is2', 'bl030105ed01is1', 'bl030105ed01is2', 'bl030203ed5is1', 'bl030203ed5is2', 'bl030303ed9is1', 'bl030303ed9is2', 'bl030504ed15is1', 'bl030504ed15is2', 'bl030602ed20is1', 'bl030602ed20is2', 'bl031103ed40is1', 'bl031103ed40is2', 'bl031201ed3is1', 'bl031201ed3is2', 'bl040202ed5is1', 'bl040202ed5is2', 'bl040302ed8is1', 'bl040302ed8is2', 'bl041102ed40is1', 'bl041102ed40is2', 'bl050104ed1is1', 'bl050104ed1is2', 'bl050503ed17is1', 'bl050503ed17is2', 'bl050704ed24is1', 'bl050704ed24is2', 'bl050802ed29is1', 'bl050802ed29is2', 'bl060103ed1is1', 'bl060103ed1is2', 'bl060502ed16is1', 'bl060502ed16is2', 'bl060904ed33is1', 'bl060904ed33is2', 'bl061204ed44is1', 'bl061204ed44is2', 'bl070102ed1is1', 'bl070102ed1is2', 'bl070205ed05is1', 'bl070205ed05is2', 'bl070403ed14is1', 'bl070403ed14is2', 'bl070604ed20is1', 'bl070604ed20is2', 'bl070703ed26is1', 'bl070703ed26is2', 'bl071002ed36is1', 'bl071002ed36is2', 'bl080304ed9is1', 'bl080304ed9is2', 'bl080402ed12is1', 'bl080402ed12is2', 'bl080702ed25is1', 'bl080702ed25is2', 'bl080903ed34is1', 'bl080903ed34is2', 'bl081104ed40is1', 'bl081104ed40is2', 'bl081203ed44is1', 'bl081203ed44is2', 'bl090204ed5is1', 'bl090204ed5is2', 'bl090603ed22is1', 'bl090603ed22is2', 'bl090804ed29is1', 'bl090804ed29is2', 'bl090902ed34is1', 'bl090902ed34is2', 'bl100105ed02is1', 'bl100105ed02is2', 'bl100203ed6is1', 'bl100203ed6is2', 'bl100303ed10is1', 'bl100303ed10is2', 'bl100504ed16is1', 'bl100504ed16is2', 'bl100602ed21is1', 'bl100602ed21is2', 'bl101103ed41is1', 'bl101103ed41is2', 'bl101201ed4is1', 'bl101201ed4is2', 'bl110202ed6is1', 'bl110202ed6is2', 'bl110302ed9is1', 'bl110302ed9is2', 'bl110803ed30is1', 'bl110803ed30is2', 'bl111102ed41is1', 'bl111102ed41is2', 'bl120104ed2is1', 'bl120104ed2is2', 'bl120503ed18is1', 'bl120503ed18is2', 'bl120704ed25is1', 'bl120704ed25is2', 'bl120802ed30is1', 'bl120802ed30is2', 'bl130103ed2is1', 'bl130103ed2is2', 'bl130502ed17is1', 'bl130502ed17is2', 'bl130904ed34is1', 'bl130904ed34is2', 'bl131104ed41is1', 'bl131104ed41is2', 'bl131204ed45is1', 'bl131204ed45is2', 'bl140102ed2is1', 'bl140102ed2is2', 'bl140205ed06is1', 'bl140205ed06is2', 'bl140403ed15is1', 'bl140403ed15is2', 'bl140604ed21is1', 'bl140604ed21is2', 'bl141002ed37is1', 'bl141002ed37is2', 'bl150304ed10is1', 'bl150304ed10is2', 'bl150402ed13is1', 'bl150402ed13is2', 'bl150702ed26is1', 'bl150702ed26is2', 'bl150903ed35is1', 'bl150903ed35is2', 'bl151203ed45is1', 'bl151203ed45is2', 'bl160204ed6is1', 'bl160204ed6is2', 'bl160603ed23is1', 'bl160603ed23is2', 'bl160804ed30is1', 'bl160804ed30is2', 'bl161202ed45is1', 'bl161202ed45is2', 'bl170105ed03is1', 'bl170105ed03is2', 'bl170203ed7is1', 'bl170203ed7is2', 'bl170303ed11is1', 'bl170303ed11is2', 'bl170504ed17is1', 'bl170504ed17is2', 'bl170602ed22is1', 'bl170602ed22is2', 'bl171103ed42is1', 'bl171103ed42is2', 'bl180202ed7is1', 'bl180202ed7is2', 'bl180302ed10is1', 'bl180302ed10is2', 'bl180803ed31is1', 'bl180803ed31is2', 'bl181004ed37is1', 'bl181004ed37is2', 'bl181102ed42is1', 'bl181102ed42is2', 'bl190104ed3is1', 'bl190104ed3is2', 'bl190404ed13is1', 'bl190404ed13is2', 'bl190503ed19is1', 'bl190503ed19is2', 'bl190704ed26is1', 'bl190704ed26is2', 'bl190802ed31is1', 'bl190802ed31is2', 'bl191101ed1is1', 'bl191101ed1is2', 'bl200103ed3is1', 'bl200502ed18is1', 'bl200502ed18is2', 'bl200904ed35is1', 'bl200904ed35is2', 'bl201003ed38is1', 'bl201003ed38is2', 'bl201204ed46is1', 'bl201204ed46is2', 'bl210102ed3is1', 'bl210102ed3is2', 'bl210205ed07is1', 'bl210205ed07is2', 'bl210604ed22is1', 'bl210604ed22is2', 'bl210703ed27is1', 'bl210703ed27is2', 'bl211002ed38is1', 'bl211002ed38is2', 'bl220304ed11is1', 'bl220304ed11is2', 'bl220402ed14is1', 'bl220402ed14is2', 'bl220702ed27is1', 'bl220702ed27is2', 'bl220903ed36is1', 'bl220903ed36is2', 'bl221104ed42is1', 'bl221104ed42is2', 'bl221203ed46is1', 'bl221203ed46is2', 'bl230204ed7is1', 'bl230204ed7is2', 'bl230603ed24is1', 'bl230603ed24is2', 'bl230804ed31is1', 'bl230804ed31is2', 'bl231202ed46is1', 'bl231202ed46is2', 'bl240203ed8is1', 'bl240203ed8is2', 'bl240303ed12is1', 'bl240303ed12is2', 'bl240504ed18is1', 'bl240504ed18is2', 'bl240602ed23is1', 'bl240602ed23is2', 'bl250302ed11is1', 'bl250302ed11is2', 'bl250803ed32is1', 'bl250803ed32is2', 'bl251004ed38is1', 'bl251004ed38is2', 'bl251102ed43is1', 'bl251102ed43is2', 'bl260104ed4is1', 'bl260104ed4is2', 'bl260404ed14is1', 'bl260404ed14is2', 'bl260503ed20is1', 'bl260503ed20is2', 'bl260802ed32is1', 'bl260802ed32is2', 'bl261101ed2is1', 'bl261101ed2is2', 'bl270103ed4is1', 'bl270103ed4is2', 'bl270502ed19is1', 'bl270502ed19is2', 'bl270904ed36is1', 'bl270904ed36is2', 'bl271003ed39is1', 'bl271003ed39is2', 'bl271204ed47is1', 'bl271204ed47is2', 'bl280102ed4is1', 'bl280102ed4is2', 'bl280403ed16is1', 'bl280403ed16is2', 'bl280604ed23is1', 'bl280604ed23is2', 'bl280703ed28is1', 'bl280703ed28is2', 'bl281002ed39is1', 'bl281002ed39is2', 'bl290304ed12is1', 'bl290304ed12is2', 'bl290402ed15is1', 'bl290402ed15is2', 'bl290702ed28is1', 'bl290702ed28is2', 'bl290903ed37is1', 'bl290903ed37is2', 'bl291104ed43is1', 'bl291104ed43is2', 'bl300603ed25is1', 'bl300603ed25is2', 'bl300804ed32is1', 'bl300804ed32is2', 'bl300902ed35is1', 'bl300902ed35is2', 'bl310105ed04is1', 'bl310105ed04is2', 'bl310303ed13is1', 'bl310303ed13is2', 'bl310504ed19is1', 'bl310504ed19is2', 'bl311201ed5is1', 'bl311201ed5is2']
****** Palestine ******
['bl010304ed8pal1', 'bl010304ed8pal2', 'bl010702ed24pal1', 'bl010702ed24pal2', 'bl010903ed33pal1', 'bl010903ed33pal2', 'bl011104ed39pal1', 'bl011104ed39pal2', 'bl011203ed43pal1', 'bl011203ed43pal2', 'bl020603ed21pal1', 'bl020603ed21pal2', 'bl020804ed28pal1', 'bl020804ed28pal2', 'bl020902ed33pal1', 'bl020902ed33pal2', 'bl021202ed44pal1', 'bl021202ed44pal2', 'bl030105ed01pal1', 'bl030105ed01pal2', 'bl030203ed5pal1', 'bl030203ed5pal2', 'bl030303ed9pal1', 'bl030303ed9pal2', 'bl030504ed15pal1', 'bl030504ed15pal2', 'bl030602ed20pal1', 'bl030602ed20pal2', 'bl031103ed40pal1', 'bl031103ed40pal2', 'bl031201ed3pal1', 'bl031201ed3pal2', 'bl040202ed5pal1', 'bl040202ed5pal2', 'bl040302ed8pal1', 'bl040302ed8pal2', 'bl041102ed40pal1', 'bl041102ed40pal2', 'bl050104ed1pal1', 'bl050104ed1pal2', 'bl050503ed17pal1', 'bl050503ed17pal2', 'bl050704ed24pal1', 'bl050704ed24pal2', 'bl050802ed29pal1', 'bl050802ed29pal2', 'bl060103ed1pal1', 'bl060103ed1pal2', 'bl060502ed16pal1', 'bl060502ed16pal2', 'bl060904ed33pal1', 'bl060904ed33pal2', 'bl061204ed44pal1', 'bl061204ed44pal2', 'bl070102ed1pal1', 'bl070102ed1pal2', 'bl070205ed05pal1', 'bl070205ed05pal2', 'bl070403ed14pal1', 'bl070403ed14pal2', 'bl070604ed20pal1', 'bl070604ed20pal2', 'bl070703ed26pal1', 'bl070703ed26pal2', 'bl071002ed36pal1', 'bl071002ed36pal2', 'bl080304ed9pal1', 'bl080304ed9pal2', 'bl080402ed12pal1', 'bl080402ed12pal2', 'bl080702ed25pal1', 'bl080702ed25pal2', 'bl080903ed34pal1', 'bl080903ed34pal2', 'bl081104ed40pal1', 'bl081104ed40pal2', 'bl081203ed44pal1', 'bl081203ed44pal2', 'bl090204ed5pal1', 'bl090204ed5pal2', 'bl090603ed22pal1', 'bl090603ed22pal2', 'bl090804ed29pal1', 'bl090804ed29pal2', 'bl090902ed34pal1', 'bl090902ed34pal2', 'bl100105ed02pal1', 'bl100105ed02pal2', 'bl100203ed6pal1', 'bl100203ed6pal2', 'bl100303ed10pal1', 'bl100303ed10pal2', 'bl100504ed16pal1', 'bl100504ed16pal2', 'bl100602ed21pal1', 'bl100602ed21pal2', 'bl101103ed41pal1', 'bl101103ed41pal2', 'bl101201ed4pal1', 'bl101201ed4pal2', 'bl110202ed6pal1', 'bl110202ed6pal2', 'bl110302ed9pal1', 'bl110302ed9pal2', 'bl110803ed30pal1', 'bl110803ed30pal2', 'bl111102ed41pal1', 'bl111102ed41pal2', 'bl120104ed2pal1', 'bl120104ed2pal2', 'bl120503ed18pal1', 'bl120503ed18pal2', 'bl120704ed25pal1', 'bl120704ed25pal2', 'bl120802ed30pal1', 'bl120802ed30pal2', 'bl130103ed2pal1', 'bl130103ed2pal2', 'bl130502ed17pal1', 'bl130502ed17pal2', 'bl130904ed34pal1', 'bl130904ed34pal2', 'bl131104ed41pal1', 'bl131104ed41pal2', 'bl131204ed45pal1', 'bl131204ed45pal2', 'bl140102ed2pal1', 'bl140102ed2pal2', 'bl140205ed06pal1', 'bl140205ed06pal2', 'bl140403ed15pal1', 'bl140403ed15pal2', 'bl140604ed21pal1', 'bl140604ed21pal2', 'bl141002ed37pal1', 'bl141002ed37pal2', 'bl150304ed10pal1', 'bl150304ed10pal2', 'bl150402ed13pal1', 'bl150402ed13pal2', 'bl150702ed26pal1', 'bl150702ed26pal2', 'bl150903ed35pal1', 'bl150903ed35pal2', 'bl151203ed45pal1', 'bl151203ed45pal2', 'bl160204ed6pal1', 'bl160204ed6pal2', 'bl160603ed23pal1', 'bl160603ed23pal2', 'bl160804ed30pal1', 'bl160804ed30pal2', 'bl161202ed45pal1', 'bl161202ed45pal2', 'bl170105ed03pal1', 'bl170105ed03pal2', 'bl170203ed7pal1', 'bl170203ed7pal2', 'bl170303ed11pal1', 'bl170303ed11pal2', 'bl170504ed17pal1', 'bl170504ed17pal2', 'bl170602ed22pal1', 'bl170602ed22pal2', 'bl171103ed42pal1', 'bl171103ed42pal2', 'bl180202ed7pal1', 'bl180202ed7pal2', 'bl180302ed10pal1', 'bl180302ed10pal2', 'bl180803ed31pal1', 'bl180803ed31pal2', 'bl181004ed37pal1', 'bl181004ed37pal2', 'bl181102ed42pal1', 'bl181102ed42pal2', 'bl190104ed3pal1', 'bl190104ed3pal2', 'bl190404ed13pal1', 'bl190404ed13pal2', 'bl190503ed19pal1', 'bl190503ed19pal2', 'bl190704ed26pal1', 'bl190704ed26pal2', 'bl190802ed31pal1', 'bl190802ed31pal2', 'bl191101ed1pal1', 'bl191101ed1pal2', 'bl200103ed3pal1', 'bl200502ed18pal1', 'bl200502ed18pal2', 'bl200904ed35pal1', 'bl200904ed35pal2', 'bl201003ed38pal1', 'bl201003ed38pal2', 'bl201204ed46pal1', 'bl201204ed46pal2', 'bl210102ed3pal1', 'bl210102ed3pal2', 'bl210205ed07pal1', 'bl210205ed07pal2', 'bl210604ed22pal1', 'bl210604ed22pal2', 'bl210703ed27pal1', 'bl210703ed27pal2', 'bl211002ed38pal1', 'bl211002ed38pal2', 'bl220304ed11pal1', 'bl220304ed11pal2', 'bl220402ed14pal1', 'bl220402ed14pal2', 'bl220702ed27pal1', 'bl220702ed27pal2', 'bl220903ed36pal1', 'bl220903ed36pal2', 'bl221104ed42pal1', 'bl221104ed42pal2', 'bl221203ed46pal1', 'bl221203ed46pal2', 'bl230204ed7pal1', 'bl230204ed7pal2', 'bl230603ed24pal1', 'bl230603ed24pal2', 'bl230804ed31pal1', 'bl230804ed31pal2', 'bl231202ed46pal1', 'bl231202ed46pal2', 'bl240203ed8pal1', 'bl240203ed8pal2', 'bl240303ed12pal1', 'bl240303ed12pal2', 'bl240504ed18pal1', 'bl240504ed18pal2', 'bl240602ed23pal1', 'bl240602ed23pal2', 'bl250302ed11pal1', 'bl250302ed11pal2', 'bl250803ed32pal1', 'bl250803ed32pal2', 'bl251004ed38pal1', 'bl251004ed38pal2', 'bl251102ed43pal1', 'bl251102ed43pal2', 'bl260104ed4pal1', 'bl260104ed4pal2', 'bl260404ed14pal1', 'bl260404ed14pal2', 'bl260503ed20pal1', 'bl260503ed20pal2', 'bl260802ed32pal1', 'bl260802ed32pal2', 'bl261101ed2pal1', 'bl261101ed2pal2', 'bl270103ed4pal1', 'bl270103ed4pal2', 'bl270502ed19pal1', 'bl270502ed19pal2', 'bl270904ed36pal1', 'bl270904ed36pal2', 'bl271003ed39pal1', 'bl271003ed39pal2', 'bl271204ed47pal1', 'bl271204ed47pal2', 'bl280102ed4pal1', 'bl280102ed4pal2', 'bl280403ed16pal1', 'bl280403ed16pal2', 'bl280604ed23pal1', 'bl280604ed23pal2', 'bl280703ed28pal1', 'bl280703ed28pal2', 'bl281002ed39pal1', 'bl281002ed39pal2', 'bl290304ed12pal1', 'bl290304ed12pal2', 'bl290402ed15pal1', 'bl290402ed15pal2', 'bl290702ed28pal1', 'bl290702ed28pal2', 'bl290903ed37pal1', 'bl290903ed37pal2', 'bl291104ed43pal1', 'bl291104ed43pal2', 'bl300603ed25pal1', 'bl300603ed25pal2', 'bl300804ed32pal1', 'bl300804ed32pal2', 'bl300902ed35pal1', 'bl300902ed35pal2', 'bl310105ed04pal1', 'bl310105ed04pal2', 'bl310303ed13pal1', 'bl310303ed13pal2', 'bl310504ed19pal1', 'bl310504ed19pal2', 'bl311201ed5pal1', 'bl311201ed5pal2']
"""