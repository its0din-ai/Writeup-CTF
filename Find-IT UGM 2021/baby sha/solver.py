import hashlib
import string

ct = [95040091416042422466109979206245377851579968489649876350018504590432341104329, 102786086251072385153811071228634563177196249010002510594959047483704227195078, 52557466141894460119325895111057743544503467879668379593769266628961900746831, 9393833428631588105965026787263253303693501820314427888153436147970358839182, 15221412158919832992695750420936616352291391591008397601210154999427198949709, 57460394973292400916472240319005124031610556156402476570691622733234139992922, 96658253242748839279896860305782247708128247298013360038597298584439466648094, 93991038469579776331861951823987231612421072636351131232401434689146807302647, 67493232492235815914836652547047482322961918992382145908913271492052854542656, 23485164565840823835255600219426697180590376765101972738474933108958799532725, 36568470624645087427742649294623092976367672819786053930004483513233096101295, 86522715239833730021281841852370880289076645518454081048135453324596289438245, 71348443431689205972649969408724287606264992461135203779596227661387843508134, 39888818818136066497120440147779195534420228065028975116798733908483071870556, 11332939448840785759738573666447790488997652263384831457761039165540623321673, 90162524081512676660399641682835345807977304869205601076775540545593005197060, 85677187248265524229543332199054080604969558778611809655543400618971274690018, 84901246698974962397641787973588877310449134839990540353828647157357598848076, 113357147350952418466820163092899299722915308057411666496361246855986364941179, 6170791294724953397389089356925835845370858668550181460004477340216566325683, 48111818384192902983778593350402141898275179744987566485197924674076469765320, 86112620412717407458620969661663672494023097930836867581688521552416521568725, 19635805597443036029464394762291551930559807070502358200170525151319954977323, 24356140627602177475454766965805297333984834946649942260763880778158458245986, 79101359951293412101123836301171490525167696646094838410411712733273339978744, 70824313509437836989690936345262173860443307868242903806722722658469044896625, 58194314696313049294389687209980907832337596519780425145548047326028257954912, 89963417126465656852115586326677821921432598421969712762035876172227530496991, 11194750070566665205982418965041456428539566154071397099061553997186711295881, 28452891461293488957203020964677558046672884131966802596197198233441601067260, 104929385741599892462581672802891344996631168940488678796554742708168653612556, 24040243626207650456041137550717820061097982408079836032156683483560980264292, 54658152314909985503821754486533727100279625536666733333944452632843565954973, 114138170134497140798052064528281089831584282908888130793143189302081131438239, 29628611720005319593144682540603017169842900318386427815238630495326524756283, 86558451385842353550587392011049248037220522960409974507043299627684835588487, 18637377541474784987479053905834067682428693971599421318724788800531772737535, 24832946272012396473228864779695351262780107363125592430316890862825040030313, 109123445864974275118795634244960887008193676969259349935601668363610146023472, 77278356700085558690968351360453947105132016435878932411176884079757970913903, 42052631084538717013873893589436105117636024941579953698383303119176958477037, 59786001505748861574218000505530518296713520449903133604479698670456687857981, 1496766755870293719281835454008717605551164372070541939696511380426111197202, 113902649969728560001009797092171671901334085635820763601409997255142045815059]

flag = ""
char = string.printable
for i in ct:
    for j in char:
        if int(hashlib.sha512((flag+j).encode()).hexdigest(), 16)>>256 == i:
            flag += j
            break

print(flag)