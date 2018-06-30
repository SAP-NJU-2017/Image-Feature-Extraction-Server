import zipfile
import json


def save_json(filename, json_str):
    with open(filename, "w") as f:
        new_dict = json.loads(json_str)
        json.dump(new_dict, f)
        print("加载入文件完成...")


def zip_files(files, zip_name):
    zip = zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED)
    for file in files:
        print('compressing', file)
        zip.write(file)
    zip.close()
    print('compressing finished')

    # files = ['.\\123.txt', '.\\3.txt']  # 文件的位置，多个文件用“，”隔开
    # zip_file = '.\\m66y.zip'  # 压缩包名字
    # zip_files(files, zip_file)


if __name__ == "__main__":
    save_json("test.json",
              "[0.0,0.0,0.17683930695056915,0.6835383176803589,0.0,0.7811245918273926,0.2617558240890503,2.4326353073120117,1.147998332977295,2.048999786376953,2.341996192932129,0.29552292823791504,0.5588304996490479,0.23447516560554504,0.1424873173236847,1.2682960033416748,0.5640079379081726,0.0,1.7434998750686646,0.2717876434326172,0.8318569660186768,0.9869426488876343,0.0,0.924881100654602,2.1145567893981934,0.3851246237754822,0.58916836977005,0.0,0.1743248850107193,1.922719955444336,2.0166194438934326,0.0,2.265225410461426,0.0,1.1787668466567993,2.238166332244873,1.238946795463562,0.8317487239837646,1.4363590478897095,1.7749738693237305,0.8599827289581299,1.3528282642364502,0.5374350547790527,0.0,1.0787849426269531,2.762528896331787,1.6429357528686523,1.5168904066085815,2.187021017074585,0.4568321704864502,2.2756943702697754,0.0,0.0,2.9953222274780273,0.0,0.19482126832008362,0.9095433950424194,0.6406814455986023,0.0,0.0,0.0,0.0,1.6675798892974854,0.0,3.5617101192474365,0.7181462049484253,0.0,0.0,0.0,1.0348209142684937,1.9305567741394043,1.0798207521438599,0.0,2.843289852142334,0.0,0.0,2.5396666526794434,0.6579923629760742,0.0,1.4104418754577637,0.6132977604866028,2.1138787269592285,0.31076815724372864,0.3406922519207001,0.7744982242584229,0.9470388889312744,0.015924543142318726,2.210455894470215,0.07017290592193604,0.03236591815948486,2.0675759315490723,0.7120213508605957,1.914163589477539,2.0640406608581543,0.7906118631362915,0.03309538960456848,0.38620316982269287,1.6948256492614746,0.6788030862808228,1.6571017503738403,0.786066472530365,0.7428089380264282,0.0,1.1450071334838867,0.8768163919448853,0.0533427894115448,2.1617634296417236,0.5387285351753235,0.4864397943019867,0.0,0.7677918672561646,0.0,0.9529105424880981,1.0941847562789917,1.2422196865081787,1.2917616367340088,0.7621175050735474,2.870321035385132,1.5487942695617676,1.6448602676391602,0.0,0.7164064645767212,0.8339714407920837,2.2893893718719482,2.027674436569214,0.0,0.8867050409317017,0.0,0.001345217227935791,0.5019961595535278,1.138139009475708,0.6089355945587158,1.4658546447753906,1.733892560005188,1.5377293825149536,0.0,1.342003345489502,0.37425753474235535,0.0,0.2905205488204956,2.338805913925171,2.84751296043396,1.168039083480835,1.024278163909912,1.8042606115341187,1.086043357849121,2.4092679023742676,0.9053322672843933,0.0,1.5306487083435059,1.0404541492462158,1.9400476217269897,0.13239768147468567,1.397371768951416,0.7056828141212463,0.6957030296325684,2.3926172256469727,0.8610400557518005,1.2324340343475342,0.0,2.190936326980591,2.1172735691070557,0.0,1.074182391166687,1.9498066902160645,0.0,0.0,1.069046139717102,2.976647138595581,1.4020686149597168,0.0,0.3285156786441803,0.0,0.26967039704322815,0.0,0.26925128698349,1.2750253677368164,1.899400234222412,0.951358437538147,0.4381510615348816,1.7228004932403564,3.971299648284912,1.820157527923584,0.4597170352935791,1.5784929990768433,0.0,0.5742725133895874,1.3606916666030884,1.8086620569229126,0.3069259524345398,0.08746308088302612,1.3712241649627686,3.0565340518951416,0.5891914367675781,1.470139503479004,0.0,0.0,1.3433395624160767,1.7007641792297363,3.19972562789917,0.7624707818031311,0.04159587621688843,2.2459447383880615,0.8017568588256836,1.6393951177597046,0.4134667217731476,0.0,1.7636370658874512,0.0,2.0585150718688965,0.7904363870620728,0.7469888925552368,0.0,0.9179712533950806,1.4277830123901367,0.0,1.4799762964248657,2.058642864227295,0.0,0.2848514914512634,1.423905611038208,0.5724226236343384,0.0,0.6910488605499268,1.1244598627090454,0.7373802661895752,1.499908447265625,0.5264674425125122,1.4674906730651855,0.45002850890159607,0.4530985355377197,1.8974412679672241,0.0,1.4985227584838867,0.01732495427131653,0.8140228986740112,0.0,0.02455538511276245,0.0,0.16520480811595917,1.6845710277557373,1.070949673652649,2.029313325881958,0.9270191192626953,0.0,1.395906925201416,0.8198656439781189,0.3864775002002716,1.6381579637527466,0.7095569372177124,0.9154384136199951,0.855682909488678,2.210293769836426,1.3507338762283325,0.0,0.44850054383277893,0.0,0.0,0.0,0.0,0.5914444923400879,0.17662498354911804,1.841805100440979,1.1158759593963623,1.1243951320648193,0.26531749963760376,0.8851513266563416,0.0,3.1360976696014404,2.1758313179016113,0.0,1.3565157651901245,1.082200527191162,0.0,2.3007559776306152,1.7872967720031738,2.494391918182373,1.6061415672302246,1.1499046087265015,2.4404544830322266,0.0,1.3820786476135254,0.7915465831756592,0.0,2.2745614051818848,0.0,0.0,0.0,2.9766886234283447,1.292193055152893,1.7508167028427124,1.3853663206100464,0.1592954844236374,3.2003469467163086,1.8878668546676636,1.8448989391326904,0.335863322019577,0.8278905749320984,1.0610520839691162,0.6410422325134277,0.769428551197052,1.3233177661895752,0.5324589610099792,2.3986358642578125,0.042864054441452026,0.772811770439148,0.6048761010169983,0.7016958594322205,0.3484201431274414,1.8423126935958862,0.6847455501556396,1.5607210397720337,0.0,0.712576150894165,0.6908763647079468,0.0,0.0,1.3712080717086792,0.929044246673584,0.0,1.3334723711013794,0.5012822151184082,2.366715908050537,1.2999783754348755,1.6226166486740112,0.0,0.8553258180618286,1.9282853603363037,0.0,1.1023672819137573,0.0,0.0,1.6010979413986206,0.46543893218040466,0.513119637966156,0.0,0.16126754879951477,1.1974297761917114,1.314624309539795,0.0,2.0490400791168213,2.601506471633911,1.062813401222229,1.2403159141540527,0.12961800396442413,1.0358648300170898,1.192515254020691,0.6029252409934998,0.2974662482738495,0.0,1.6597791910171509,0.5717024803161621,0.0,0.0,0.0,1.4473568201065063,2.589170217514038,0.4623599648475647,2.30198335647583,1.1476860046386719,1.175341248512268,2.229583501815796,0.5546611547470093,0.9857562780380249,1.600777268409729,3.7881147861480713,1.1886619329452515,0.0,1.8982094526290894,0.7666221857070923,1.9284521341323853,2.066322088241577,0.0,2.9763238430023193,0.3620666265487671,0.44499439001083374,0.0,0.9447122812271118,0.0490855872631073,1.5852771997451782,0.0,0.9547833204269409,1.8211908340454102,0.0,2.809305191040039,2.246824026107788,1.4447245597839355,1.4154125452041626,0.0,0.0,2.5056209564208984,2.46486496925354,1.9370355606079102,0.5230773687362671,0.3841714560985565,0.46642911434173584,0.7062199711799622,2.227973699569702,0.0,0.8912118673324585,0.7504391670227051,0.0,0.40650105476379395,2.2202115058898926,0.556270182132721,3.5430145263671875,0.32557931542396545,0.8701752424240112,1.4010021686553955,1.6504755020141602,1.062684178352356,0.17989793419837952,0.0,0.6428124904632568,2.304363965988159,0.0,3.5356929302215576,0.09798893332481384,2.601377248764038,1.3331472873687744,0.4927031397819519,0.0,1.062401533126831,2.461301565170288,2.446075916290283,1.9472508430480957,0.2596498727798462,0.2188364416360855,1.3210289478302002,0.0,0.14745602011680603,0.3180548846721649,0.4044680595397949,0.0,1.242347002029419,1.36799156665802,0.0,2.9641776084899902,0.4148223400115967,0.5509750247001648,2.3618319034576416,0.8075311183929443,1.8180400133132935,0.9189677834510803,0.6153222322463989,0.4363342523574829,2.2880475521087646,0.0,2.1950347423553467,3.0162527561187744,0.0,0.0,0.22337165474891663,2.6376793384552,0.9476190209388733,1.7115141153335571,0.8972921371459961,1.7020366191864014,1.3408311605453491,0.0,0.0,1.520703673362732,0.25184088945388794,1.4224517345428467,1.627333402633667,1.3263845443725586,1.842985987663269,0.9341096878051758,1.2082269191741943,2.2809765338897705,0.030084818601608276,0.8263037800788879,0.0,2.413367748260498,1.7936012744903564,0.8248718976974487,0.0,0.7198593616485596,2.7731480598449707,0.0,0.6833624839782715,0.0,0.7712537050247192,1.4740415811538696,1.5870532989501953,0.0,1.313004493713379,1.3025555610656738,0.5752859115600586,1.9168312549591064,1.646702766418457,0.0,1.7292536497116089,0.0,0.0,0.0,1.3034989833831787,0.3500131070613861,1.0756746530532837,1.4023605585098267,0.0,1.1155275106430054,0.5837006568908691,1.0429141521453857,0.0,1.090553641319275,0.7196154594421387,0.3939858675003052,0.520439088344574,0.09999102354049683,2.749145984649658,0.0,1.0927190780639648,0.0,0.632071316242218,0.0,0.6149681806564331,1.6030588150024414,1.4973092079162598,0.0,1.8319835662841797,2.385331153869629,0.861716628074646,0.9614940881729126,0.8274972438812256,0.0,0.05062195658683777,0.1483604609966278,0.0,0.52379310131073,1.3973177671432495,1.5079385042190552,0.26633089780807495,1.1334455013275146,0.28331321477890015,0.7324104309082031,0.0,1.8640155792236328,0.3988812267780304,0.868675708770752,0.0,1.3976621627807617,2.157487392425537,0.0,2.1747517585754395,0.0,1.8952698707580566,0.6201246976852417,1.1107882261276245,0.0,0.6244810819625854,0.0,0.12889905273914337,0.1472090482711792,0.8625621795654297,0.0,3.5124106407165527,0.0,2.935176134109497,1.5700920820236206,0.0,0.0,0.7430055141448975,1.5946986675262451,2.1176702976226807,0.5327802896499634,0.5531500577926636,0.17527423799037933,0.0,2.185314655303955,0.7702849507331848,0.0,0.7341915369033813,0.7706230878829956,0.6867586970329285,1.2405905723571777,0.5514136552810669,2.1196672916412354,1.1871962547302246,0.6221635341644287,0.0,0.801082968711853,2.4657320976257324,1.880440592765808,0.0,0.6542896032333374,0.20131105184555054,0.22077268362045288,1.0138516426086426,3.3574047088623047,1.3847389221191406,0.0,1.7568492889404297,1.812624216079712,2.3367106914520264,0.7589014768600464,0.0,2.9961538314819336,0.9856489896774292,2.27302622795105,0.0,1.135603427886963,1.6518563032150269,0.8851088881492615,0.0,0.22724774479866028,0.46803316473960876,0.4598333239555359,0.5205733776092529,0.0,0.4275985360145569,1.604559063911438,0.0,2.339115858078003,1.9246044158935547,2.0145318508148193,1.3768470287322998,1.3814811706542969,1.1451311111450195,0.0,2.8013103008270264,1.7445627450942993,0.0,1.3773219585418701,0.0,0.0,1.2341361045837402,0.8670464754104614,0.4702465832233429,1.6230809688568115,0.4516902565956116,1.9272557497024536,1.7752400636672974,1.7421319484710693,0.7497987747192383,1.7593660354614258,0.0,0.7561224102973938,0.7931330800056458,0.3696679472923279,2.155029773712158,1.665034294128418,1.533949613571167,1.0640778541564941,0.6349515914916992,0.0,0.9286726713180542,1.0813437700271606,3.0734057426452637,0.7833876609802246,0.0,0.0,0.15998689830303192,0.7463229298591614,0.890778124332428,0.0,0.06391924619674683,0.5530600547790527,2.0079758167266846,3.4202966690063477,1.0802292823791504,2.3723788261413574,0.6929830312728882,2.0777034759521484,1.3099215030670166,1.6589863300323486,1.7624058723449707,0.0,0.4283151924610138,0.0,0.3554229438304901,0.41865283250808716,3.326327323913574,0.6646503210067749,1.7283401489257812,2.290731906890869,2.008019208908081,1.244375467300415,0.7450027465820312,0.7312082648277283,2.0353219509124756,0.0,0.7106582522392273,0.0,1.4370461702346802,2.473287582397461,0.0,2.180481195449829,1.4179967641830444,0.6805988550186157,0.9785346984863281,2.6813650131225586,0.0,1.585128903388977,0.7595879435539246,0.38447776436805725,0.819090723991394,1.6812750101089478,0.8369512557983398,0.0,0.0,1.1363353729248047,0.17284099757671356,0.058487385511398315,0.38939106464385986,0.8331054449081421,0.0,0.5968210697174072,0.1870398074388504,0.7358130216598511,0.8035097122192383,0.9719278812408447,0.9974367618560791,1.454100251197815,2.14726185798645,0.12756162881851196,0.0,1.8530731201171875,0.5523436665534973,0.853553056716919,0.0,0.0,0.8128911852836609,1.7057726383209229,0.8181412220001221,4.055055618286133,2.6297054290771484,0.0,1.0653306245803833,2.492908000946045,0.617179274559021,0.20524388551712036,0.0,0.8859314322471619,0.0,0.33578187227249146,0.21188902854919434,0.0,1.4275083541870117,0.0,0.0,0.5306704044342041,0.4847629964351654,0.0,0.0,1.1633901596069336,0.0,0.0,0.9019598960876465,0.0,2.066898822784424,0.8348387479782104,0.0,1.8020612001419067,2.3040497303009033,1.6357336044311523,0.0,1.4235337972640991,0.7969614267349243,0.6785401701927185,0.0,1.9672598838806152,2.4360198974609375,0.5867576003074646,0.06264358758926392,1.4704240560531616,0.0,0.8126103281974792,3.3461551666259766,0.8382307291030884,1.6128028631210327,0.0,0.13588306307792664,2.129817485809326,1.5201648473739624,0.30020231008529663,1.2935090065002441,2.2937700748443604,1.0988202095031738,0.8748917579650879,1.017875075340271,0.3026663064956665,0.0,0.48252856731414795,1.2847230434417725,1.588205337524414,1.2899651527404785,1.5362985134124756,0.008001238107681274,2.5366384983062744,1.5619866847991943,1.9019384384155273,2.3634612560272217,2.408160448074341,0.06814739108085632,0.0,2.2000255584716797,0.4379809498786926,0.0,0.0,2.157564163208008,1.9765602350234985,1.26613450050354,1.4296789169311523,0.0,0.0,2.00433087348938,1.7642165422439575,0.671058177947998,2.186767816543579,1.8021881580352783,1.180985450744629,1.2439639568328857,0.0,2.7862753868103027,0.02429792284965515,0.0,1.1931719779968262,0.9792863726615906,1.5674183368682861,1.3046576976776123,0.9576483368873596,0.14250048995018005,1.3293763399124146,1.9877859354019165,2.275857925415039,0.24647454917430878,0.2603622376918793,1.7977486848831177,0.0,0.4124651551246643,0.0,1.3544628620147705,0.0,0.27482879161834717,0.0,0.5928556323051453,1.45969557762146,1.4128410816192627,1.1003458499908447,0.0,1.4147229194641113,0.0,0.0,3.165192127227783,0.8541315793991089,2.11877703666687,0.9070260524749756,0.3045028746128082,1.5121502876281738,0.928925633430481,1.4086008071899414,0.7870634198188782,1.4126967191696167,0.22734041512012482,0.9562421441078186,2.12007737159729,1.2474349737167358,0.26322808861732483,1.7063055038452148,1.685962200164795,0.0,1.1862748861312866,0.0,0.0,1.0584399700164795,1.7759709358215332,0.9447107911109924,0.0,0.0,0.7223601341247559,0.0,0.9388196468353271,0.021409034729003906,0.9836117029190063,0.0,0.9344441890716553,1.4306732416152954,0.0,1.15131413936615,1.2548409700393677,1.8703136444091797,2.853996753692627,1.015250563621521,1.9114125967025757,2.5178611278533936,1.885664463043213,0.7351894378662109,0.0,2.3062734603881836,2.7130439281463623,1.9893397092819214,1.7916560173034668,0.0,1.8839318752288818,0.0,1.7354986667633057,0.028285831212997437,0.0,1.9389004707336426,0.4998715817928314,0.0,0.6242510080337524,1.5569759607315063,1.6684379577636719,1.7785731554031372,0.9701043963432312,0.0,2.973588466644287,2.5355734825134277,1.5275142192840576,0.6722922325134277,0.12238603830337524,1.4537971019744873,0.0,2.2246971130371094,0.0,3.2863545417785645,1.1670000553131104,1.701322317123413,0.0,1.42476487159729,1.1856940984725952,0.6867517232894897,1.8861708641052246,0.8223559856414795,1.4412362575531006,0.031172215938568115,0.6378511190414429,0.7477782964706421,0.0,1.4163179397583008,0.9925196170806885,2.156240463256836,0.9663404226303101,1.606622338294983,1.9375238418579102,0.3124365508556366,2.6969759464263916,0.6619141101837158,0.47861936688423157,1.5416767597198486,0.0,1.1178685426712036,0.0,0.0,1.204131007194519,3.2088537216186523,1.3221571445465088,2.2132742404937744,0.47341665625572205,0.27577847242355347,0.0,1.843113660812378,0.9225770235061646,0.523388147354126,2.528343677520752,0.1942935436964035,2.685028076171875,0.0,1.5419894456863403,0.9311756491661072,1.1798087358474731,0.0,1.2870116233825684,0.0,0.2667733430862427,1.255692720413208,1.4364066123962402,0.0,0.9514523148536682,0.009765267372131348,1.2345057725906372,2.2707440853118896,0.451751708984375,0.321188360452652,0.6436591148376465,1.0912301540374756,2.3279263973236084,2.677910089492798,0.0,1.6053361892700195,0.8573902249336243,0.9348771572113037,0.2901652157306671,2.6667351722717285,1.5012645721435547,0.20709070563316345,0.03450539708137512,1.7996234893798828,2.8133068084716797,0.0,2.1362533569335938,1.3462703227996826,1.8764665126800537,1.7071284055709839,0.0,2.4828848838806152,1.455352783203125,1.9858607053756714,0.0,0.5511818528175354,0.03460356593132019,0.18398171663284302,0.0,1.162570834159851,0.8248785734176636,1.5873985290527344,0.0,0.8729593753814697,1.2140650749206543,2.3560657501220703,3.6504526138305664,3.937990427017212,0.1854541003704071,0.9142036437988281,0.945014238357544,2.0235538482666016,0.710477352142334,0.5420836210250854,0.0,0.0,3.1810688972473145,0.9812061786651611]")
