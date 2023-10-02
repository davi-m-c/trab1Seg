texto_para_decifrar = "rvgllakieg tye tirtucatzoe.  whvnvvei i winu mpsecf xronieg giid abfuk thv mfuty; wyenvvvr ik ij a drmg, drzzqly eomemsei in dy jouc; wyenvvvr i wied mpsvlf znmollnkarzlp palszng seworv cfffzn narvhfusvs, rnd srzngznx up khv rerr ff emeiy flnvrac i deek; aed ejpvcirlcy wyeeevvr dy hppfs gvt jucy ae upgei haed ff mv, tyat zt ieqliies r skroeg dorrl grieczplv tf prvvvnt de wrod dvliseiatvlp stvpginx ieto khv stievt, aed detyouicrlcy keotkieg geoglv's hrtj ofw--tyen, z atcolnk it yixh tzmv to xek to jer as jofn aj i tan.  khzs ij mp susskitltv foi pzstfl rnd sacl.  wzty a pyicosfpyicrl wlolrzsh tako tyrfws yidsecf lpoe hzs snoid; i huzetcy kakv tf thv syip.  khvre zs eotyieg slrgrijieg ie tyis.  zf khep blt keen it, rldosk acl mvn zn tyezr dvgiee, jode tzmv or ftyer, thvrijh merp nvarcy khe jade fvecinxs kowrrus tye fcern nity mv."
lang_freq = [0.08167, 0.01492, 0.02782, 0.04253, 0.12702, 0.02228, 0.02015, 0.06094, 0.06966, 0.00153, 0.00772, 0.04025, 0.02406, 0.06749, 0.07507, 0.01929, 0.0095, 0.05987, 0.06327, 0.09056, 0.02758, 0.00978, 0.0236, 0.0015, 0.01974, 0.00074]
def tamanhoDaChave(textocifrado):
    factors = [0] * 22
    for i in range(len(textocifrado)-2):
        trigrama=textocifrado[i:i+3]
        for j in range(i+3,len(textocifrado)-2):
            if textocifrado[j:j+3] == trigrama:
                distancia = j-(i+2)
                #print(trigrama,distancia)
                for k in range(2, 22):
                    if distancia%k==0:
                        factors[k]+=1
                break   
                
    print("Tamanhos de chaves e sua quantidade de fatores encontrada :")
    for i in range(2,len(factors)):
        print(f'\t{i} - {factors[i]}')
    selected = int(input('Selecione o tamanho da chave desejada:'))
    return selected 

letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
def calcular_freq(texto):
    total_caracteres = len(texto)
    contagem = [0] * 26
    
    for letra in texto:
        if letra.isalpha():
            n=0
            for let in letras:
                if letra.lower() == let:
                    indice = n
                n+=1
            contagem[indice] += 1
    n=0
    for x in contagem:
        contagem[n]=x/total_caracteres
        n+=1
    return contagem
frequencia = calcular_freq(texto_para_decifrar)
#print(frequencia)
def analise_frequencia(textocifrado):
    freq = calcular_freq(textocifrado)
    dif = []
    for j in range(26):
        score = sum([lang_freq[i] * freq[i] for i in range(26)])
        dif.append(score)
        freq.append(freq.pop(0))
    return dif.index(max(dif))
for n in range(tamanhoDaChave(texto_para_decifrar)):
    print(analise_frequencia(texto_para_decifrar))