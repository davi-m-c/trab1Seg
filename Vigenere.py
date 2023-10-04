from unidecode import unidecode
import string
def cifrador(mensagem,chave):
    #passando a mensagem para minusculo
    mensagem = mensagem.lower()
    #removendo espacos, se houver, na mensagem
    while(" " in mensagem):
        mensagem = mensagem.replace(" ","")
    #lista das letras posicionadas
    letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    chavecheia=""
    #adicionando na chave inteira o correspondente da chave, se for uma letra, ou um asterisco, q siginifica q o caracter nao vai ser cifrado, se for uma pontuacao ou letra acentuada
    n=0
    for caracter in mensagem:
        testa_acento = unidecode(caracter)
        if (caracter != testa_acento) or (caracter in string.punctuation) or (caracter in string.digits):
            chavecheia+="*"
        else:
            if n>=len(chave):
                n=n-len(chave)
            chavecheia+=chave[n]
            n+=1
    criptograma=""
    #deslocando cada letra da mensagem pela chave para formar o criptograma
    n=0
    for letra in mensagem:
        testa_acento = unidecode(letra)
        if (letra != testa_acento) or (letra in string.punctuation) or (letra in string.digits):
            criptograma+=letra
        else:
            numero_da_proxima = letras.index(letra) + letras.index(chavecheia[n])
            while(numero_da_proxima>=26):
                numero_da_proxima-=26
            proxima_letra = letras[numero_da_proxima]
            criptograma+=proxima_letra
        n+=1
    print(criptograma)

def decifrador(mensagem,chave):
    #passando a mensagem para minusculo
    mensagem = mensagem.lower()
    #removendo espacos, se houver, na mensagem
    while(" " in mensagem):
        mensagem = mensagem.replace(" ","")
    #lista das letras posicionadas
    letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    chavecheia=""
    #adicionando na chave inteira o correspondente da chave, se for uma letra, ou um asterisco q siginifica q o caracter nao vai ser cifrado se for uma pontuacao ou letra acentuada
    n=0
    for caracter in mensagem:
        testa_acento = unidecode(caracter)
        if (caracter != testa_acento) or (caracter in string.punctuation) or (caracter in string.digits):
            chavecheia+="*"
        else:
            if n>=len(chave):
                n=n-len(chave)
            chavecheia+=chave[n]
            n+=1
    msgdecifrada=""
    #deslocando cada letra da mensagem pela chave para decifrar
    n=0
    for letra in mensagem:
        testa_acento = unidecode(letra)
        if (letra != testa_acento) or (letra in string.punctuation) or (letra in string.digits):
            msgdecifrada+=letra
        else:
            numero_da_proxima = letras.index(letra) - letras.index(chavecheia[n])
            while(numero_da_proxima>=26):
                numero_da_proxima-=26
            proxima_letra = letras[numero_da_proxima]
            msgdecifrada+=proxima_letra
        n+=1
    print(msgdecifrada)
#decifrador("tpsja kexis ttgztpb wq ssmil tfdxf vsetw ytafrttw btzf pcbroxdzo zn tqac wix, bwfd s, je ahvup sd pcbqqxff lfzed d avu ytwoxavneh sg p aznst qaghv. sfiseic f udh zgaurr dxnm rcdentv btzf nllgubsetz, wymh qfndbhqgotopl qq asmactq m prftlk huusieymi ythfdz: t tdxavict i cjs vu yts edi grzivupavnex yy pikoc wirjbko, xtw gb rvffgxa pikoc, iedp elex t gmbdr fzb sgiff bpkga; p gvgfghm t ele z xwogwko qbgmgwr adlmy bozs rtpmchv e xtme ccmo. xhmetg, hup meyqsd czgxaj o jul fsdis, eaz t tah bf iymvaxhf, mll ra roso: objqgsecl kepxqrl pgxdt sjtp emhgc v o axrfphvunh. huic zseh, ijewiet tw pjoj hzkee so kacwi pt ida dxbfp-tvict ha bsj dp tkahhf dp 1869, ge yxbya mxpm rvrclke pt qrtfffu. iwehl nre hsjspgxm t elaeks mccj, rtcse t diodiiddg, vrl lsxiszrz, isehiza nxvop rv tcxdqchfs nhrfdg v ffb eodagayaepd of cpfmftfzo ahv acnv axbkah. cezp tquvcj! vpkhmss v qfx rmd vfugx gmghrs yxq mciecthw. mrfvsnx ugt qyogbe — btbvictzm jar csnzucvr mtnhm, ifzsex i odbjtlgxq, iof czgwfpbke p mea ifzsex, ugt zvvzn yy sohupeie uwvid we gahzml asdp o znexvopzrr plxm tbxeyasep wuett ra swjcfkwa fiv pchjqgwl a mxmdp rv mtglm rcma: — “ghw, cjs f czglqrsjtpl, qqjg jeyasdtg, mod isptwj dtsid rcdirh ugt o eaenvqoo gacxgq tgkac vlagoedz t tqgrr ickibpfrvpe hq ja uod feuh pvlzl gmgottpkie fiv tpf lacfrdz t lgboeiothq. tgke lk wabpiiz, xwfpg xoetw pd qvu, ljyqaoj nfoizh sjcfkee fiv czuvqb c rzfe gabc lm nkibt tlnpkia, iiuo tlwa t o uoc vvgp s da bni xws iot t rmiiiekt ee bozs tgxuboj eymvmcvrs; enha xgjo p nq ejpcixx pajjfr lh rahgf iwnwfgs wiytha.” qcd e qbix pazgz! gea, cof mp tvdtdvnoh hmh jznex ebdzzcpl ugt zye oxmjtw. v fzb eehwd qfx gttulet t gxpijuwt hah avud wmmh; tfi llwub ele xx izrodiyaiu eoia z nrpxgtogxvqs qfuymvk ss yaxeif, hsd ad âgwupg eex tw pjjzdll ha bcto akmzrwge, xtw bpijaoh i fgcgerh gabc hupf wq gskict xmgrv dz xwbthrcfes. fpfue p tfagfvctws. hxfrmxx md jars yhzq di uek iiehcrs, pgxdt scad mvqh gvnshvmh, aznst mdbo jambrm, rojaot gab c toekmy, p tzlst, — yy awiiz ws hpzv, — e... exrtpa ganbizrwr! dljyu p dfunh pttg uicxm cjsd ect e ftftetke etbyoct. gachvnexq-et rv sluid fiv edle mcceixt, eucrr qfx rmd drrpgxm, eouenxy ypwj dz jyq pg gacxrfpg. v vpkhmss, gaoxgqj arid. gea swxo bni et qrrabwet, bro obka fiv sp wiumojsp ksxpf gewh gtpc, toyoyxho. eex h qqj csieh idp qfidt exiodeymi pgodaebgm... ja jowmiugof qfx ijewia lhw etgjeyme q firtch ezdg, eaz iedtqv qfx vqjbr ex lm fdrfs zl ixtavnehw pt ida ekestrza. p wepd ele dbq, a fiv mpgse rcevtglm p sjsl tracwda pke meoieyme-xd. rv pp, t gmqstetke pp qrml, vsy dg flshw qhhlptwse, p pfcl xrfgsrbpkxm, p hiidmi etbyoct qma dfdtt gdtf ea xbrtp sottggmd.",'temporal')
#decifrador("rvgllakieg tye tirtucatzoe.  whvnvvei i winu mpsecf xronieg giid abfuk thv mfuty; wyenvvvr ik ij a drmg, drzzqly eomemsei in dy jouc; wyenvvvr i wied mpsvlf znmollnkarzlp palszng seworv cfffzn narvhfusvs, rnd srzngznx up khv rerr ff emeiy flnvrac i deek; aed ejpvcirlcy wyeeevvr dy hppfs gvt jucy ae upgei haed ff mv, tyat zt ieqliies r skroeg dorrl grieczplv tf prvvvnt de wrod dvliseiatvlp stvpginx ieto khv stievt, aed detyouicrlcy keotkieg geoglv's hrtj ofw--tyen, z atcolnk it yixh tzmv to xek to jer as jofn aj i tan.  khzs ij mp susskitltv foi pzstfl rnd sacl.  wzty a pyicosfpyicrl wlolrzsh tako tyrfws yidsecf lpoe hzs snoid; i huzetcy kakv tf thv syip.  khvre zs eotyieg slrgrijieg ie tyis.  zf khep blt keen it, rldosk acl mvn zn tyezr dvgiee, jode tzmv or ftyer, thvrijh merp nvarcy khe jade fvecinxs kowrrus tye fcern nity mv.",'arara')
cifrador("algumtempohesiteisedeviaabrirestasmemoriaspeloprincipiooupelofim,istoe,seporiaemprimeirolugaromeunascimentoouaminhamorte.supostoousovulgarsejacomecarpelonascimento,duasconsideracoesmelevaramaadotardiferentemetodo:aprimeiraequeeunaosoupropriamenteumautordefunto,masumdefuntoautor,paraquemacampafoioutroberco;asegundaequeoescritoficariaassimmaisgalanteemaisnovo.moises,quetambemcontouasuamorte,naoaposnointroito,masnocabo:diferencaradicalentreestelivroeopentateuco.ditoisto,expireiasduashorasdatardedeumasexta-feiradomesdeagostode1869,naminhabelachacaradecatumbi.tinhaunssessentaequatroanos,rijoseprosperos,erasolteiro,possuiacercadetrezentoscontosefuiacompanhadoaocemiterioporonzeamigos.onzeamigos!verdadeequenaohouvecartasnemanuncios.acrescequechovia—peneiravaumachuvinhamiuda,tristeeconstante,taoconstanteetaotriste,quelevouumdaquelesfieisdaultimahoraaintercalarestaengenhosaideianodiscursoqueproferiuabeirademinhacova:—“vos,queoconhecestes,meussenhores,vospodeisdizercomigoqueanaturezapareceestarchorandoaperdairreparaveldeumdosmaisbeloscaracteresquetemhonradoahumanidade.estearsombrio,estasgotasdoceu,aquelasnuvensescurasquecobremoazulcomoumcrepefunereo,tudoissoeadorcruaemaquelheroianaturezaasmaisintimasentranhas;tudoissoeumsublimelouvoraonossoilustrefinado.”bomefielamigo!nao,naomearrependodasvinteapolicesquelhedeixei.efoiassimquechegueiaclausuladosmeusdias;foiassimquemeencaminheiparaoundiscoveredcountrydehamlet,semasânsiasnemasduvidasdomocoprincipe,maspausadoetropegocomoquemseretiratardedoespetaculo.tardeeaborrecido.virammeirumasnoveoudezpessoas,entreelastressenhoras,minhairmasabina,casadacomocotrim,afilha,—umliriodovale,—e...tenhampaciencia!daquiapoucolhesdireiquemeraaterceirasenhora.contentem-sedesaberqueessaanonima,aindaquenaoparenta,padeceumaisdoqueasparentas.everdade,padeceumais.naodigoquesecarpisse,naodigoquesedeixasserolarpelochao,convulsa.nemomeuobitoeracoisaaltamentedramatica...umsolteiraoqueexpiraaossessentaequatroanos,naoparecequereunaemsitodososelementosdeumatragedia.edadoquesim,oquemenosconvinhaaessaanonimaeraaparenta-lo.depe,acabeceiradacama,comosolhosestupidos,abocaentreaberta,atristesenhoramalpodiacrernaminhaextincao.","temporal")
#cifrador("regulatingthecirculation.wheneverifindmyselfgrowinggrimaboutthemouth;wheneveritisadamp,drizzlynovemberinmysoul;wheneverifindmyselfinvoluntarilypausingbeforecoffinwarehouses,andbringinguptherearofeveryfuneralimeet;andespeciallywhenevermyhyposgetsuchanupperhandofme,thatitrequiresastrongmoralprincipletopreventmefromdeliberatelysteppingintothestreet,andmethodicallyknockingpeople'shatsoff--then,iaccountithightimetogettoseaassoonasican.thisismysubstituteforpistolandball.withaphilosophicalflourishcatothrowshimselfuponhissword;iquietlytaketotheship.thereisnothingsurprisinginthis.iftheybutknewit,almostallmenintheirdegree,sometimeorother,cherishverynearlythesamefeelingstowardstheoceanwithme.","arara")
