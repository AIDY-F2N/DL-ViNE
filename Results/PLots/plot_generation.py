
import matplotlib.pyplot as plt
import numpy as np

# Données simulées
#variable =  [0.02, 0.03, 0.04, 0.045, 0.05,0.055, 0.06, 0.065, 0.07, 0.075, 0.08] #lambda
#variable = [45, 48, 50, 53, 55, 58, 60, 65, 70] #ressources
#variable = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19] #slice
variable = [50, 60, 70,80, 90, 100] #physical
#Ressources
#variable = [35, 40, 45, 50, 55, 60]

# Calcul des valeurs moyennes pour les taux d'acceptation 
'''
Maxime = [0.56018, 0.6401, 0.6858399999999999, 0.77024, 0.7823799999999999, 0.86126]
Nrpa_c = [0.3841800000000001, 0.32526, 0.27112, 0.23569999999999997, 0.1451, 0.09224]
Nrpa = [0.00216, 0.00018, 0.0, 0.0, 0.0, 0.0]
Nepa_c = [0.38404000000000005, 0.312, 0.23695999999999998, 0.21018000000000003, 0.12947999999999998, 0.06984]
'''
#REVENUES
Maxime = [0.9949465858255697, 0.9198935824839911, 0.8525311170399699, 0.8443881634392039, 0.805311254649213, 0.849549979044809]
Nrpa_c = [1.5029713049302043, 1.4930727376990085, 1.4781940042790065, 1.4486597263460521, 1.3772062760581267, 1.4093150788134803]
Nrpa = [0.7277797795580058, 0.08843161515715807, 0.0, 0.0, 0.0, 0.0]
Nepa_c = [1.4951261546357233, 1.4798327027340665, 1.4826654721255463, 1.4456845989471243, 1.3952683106107628, 1.3851398581035543]

# Création du plot
plt.figure(figsize=(10, 5))
plt.plot(variable, Maxime, marker='v', color='gray', linestyle='--', label='NEPA(Path)')
#plt.plot(variable, Nepa_c, marker='x', color='#A9A9A9', linestyle='--', label='NEPA-DLPlus')
plt.plot(variable, Nrpa_c, marker='s', color='#3357FF', linestyle='-', label='NRPA-DLPlus')
plt.plot(variable, Nrpa, marker='o', color='black', linestyle='-', label='NRPA-DL')



plt.xticks(fontsize=14)  # Agrandir les valeurs sur l'axe x
plt.yticks(fontsize=14)  # Agrandir les valeurs sur l'axe y

# Ajout de titres et de labels 33FF57
#plt.xlabel('Arrival rate', fontsize=14)
#plt.xlabel('Mean number of ressources',fontsize=14)
#plt.xlabel('Mean number of virtual nodes',fontsize=14)
plt.xlabel('Size of physical network',fontsize=14)

#plt.xlabel('Mean BW on physical links',fontsize=14)
#plt.xlabel('Mean CPU on physical nodes',fontsize=14)
#plt.xlabel('Mean ressources on physical network',fontsize=14)

#plt.ylabel('Acceptance ratio', fontsize=14)
plt.ylabel('Revenue-to-cost ratio', fontsize=14)

plt.legend().remove()
#plt.legend(fontsize=18, loc='lower right', bbox_to_anchor=(1, 0.15))
#plt.legend(fontsize=18)
#plt.ylim(0.94, 1.5)
# Affichage du graphique
plt.grid(True)
plt.show()


'''
#Résultats graphe non complet 500 slices 6 algos"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

********* Lambda
Maxime =   [1.0, 0.9732000000000001, 0.8014, 0.8413999999999999, 0.7998, 0.7442000000000001, 0.695, 0.5706, 0.6206, 0.5936, 0.5598]
Nrpa_c = [0.5442, 0.5116, 0.4898, 0.4776, 0.4584, 0.447, 0.43539999999999995, 0.4308, 0.414, 0.4074, 0.38580000000000003]
Nrpa=     [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
Nepa_c = [0.507, 0.49060000000000004, 0.468, 0.4606, 0.45080000000000003, 0.438, 0.4328, 0.4174, 0.4174, 0.4028, 0.38680000000000003]

#REVENUES
Maxime = [1.2767896318950167, 1.1607251256938267, 0.9462695346953858, 1.0246162452788845, 0.9870123918689853, 0.975006205023468, 0.9575121588910896, 0.8386424447143472, 0.904394801372588, 0.8977737226489981, 0.8959867669899386]
Nrpa_c = [1.4783384932115553, 1.477905567517756, 1.48380026643336, 1.481563614625314, 1.4770497606874884, 1.4837332717065541, 1.488039626079948, 1.4869071870078145, 1.4853551878121452, 1.4795846231879213, 1.4932322151809378]
Nrpa = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
Nepa_c = [1.4734299543616625, 1.4840683063117066, 1.4884853925007564, 1.4859896870429679, 1.4831594609565872, 1.4954782865310159, 1.4900618659763423, 1.4988712418761132, 1.49633982571441, 1.4862984292563761, 1.5025944325275513]

********** Ressources
Maxime = [0.7526, 0.8306, 0.8702000000000001, 0.926, 0.95, 0.9728, 0.9798, 0.9894, 0.998]
Nrpa_c = [0.19340000000000002, 0.21819999999999998, 0.2364, 0.26880000000000004, 0.295, 0.33039999999999997, 0.355, 0.4176, 0.4746]
Nrpa = [0.0002, 0.0, 0.0, 0.0, 0.0, 0.0004, 0.0002, 0.0, 0.0]
Nepa_c = [0.1762, 0.197, 0.2226, 0.2464, 0.2666, 0.3024, 0.32, 0.384, 0.4482] 

#REVENUES
Maxime = [0.8694044586954138, 0.9020113197319943, 0.922077893057023, 0.9661978998811325, 0.9992117489315178, 1.0512361011747824, 1.081833658061664, 1.159414403625826, 1.220444012134307]
Nrpa_c = [1.3888963887128567, 1.3921913397844907, 1.4020265484757712, 1.4085660715111838, 1.417191590410144, 1.4192522122282627, 1.4358591820113158, 1.448052137225996, 1.4611068917982004]
Nrpa = [0.11589958158995817, 0.0, 0.0, 0.0, 0.0, 0.21417624521072795, 0.11417624521072797, 0.0, 0.0]
Nepa_c = [1.4079560784968455, 1.4280567199017793, 1.4280300325165234, 1.434128054377471, 1.423649505709594, 1.4280338417251728, 1.4290111766967621, 1.4395919330774054, 1.4561048136915524]

********** Slice
Maxime = [1.0, 0.9994, 0.988, 0.9458, 0.923, 0.8832000000000001, 0.8204, 0.7328, 0.6644, 0.6008]
Nrpa_c = [0.4382, 0.30939999999999995, 0.2508, 0.1546, 0.083, 0.0644, 0.026199999999999998, 0.0136, 0.003, 0.0006]
Nrpa = [0.0002, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
Nepa_c = [0.4102, 0.2718, 0.2356, 0.139, 0.0746, 0.054200000000000005, 0.0258, 0.0134, 0.0024, 0.0014]

#REVENUES
Maxime = [1.2162421962795913, 1.120603721100547, 1.062168997348174, 0.9637922313494756, 0.903377768960931, 0.8692080220838763, 0.8212255594977366, 0.7644275026290704, 0.7321041368340628, 0.6978747433886587]
Nrpa_c = [1.4756029342548103, 1.470794413429206, 1.4425726878904344, 1.3686600639339646, 1.4297827648270212, 1.3496132089145498, 1.3163014363012615, 1.369923900080243, 1.1561992972409156, 0.3853421627908705]
Nrpa = [0.101417004048583, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
Nepa_c = [1.4645586671605533, 1.4554178157740527, 1.4256386482890266, 1.3959528259005765, 1.3890864033332402, 1.335648674662446, 1.2952892471204838, 1.3184491676880281, 0.9293342680763657, 0.740883862520414]

********** Physical
Maxime = [0.56018, 0.6401, 0.6858399999999999, 0.77024, 0.7823799999999999, 0.86126]
Nrpa_c = [0.3841800000000001, 0.32526, 0.27112, 0.23569999999999997, 0.1451, 0.09224]
Nrpa = [0.00216, 0.00018, 0.0, 0.0, 0.0, 0.0]
Nepa_c = [0.38404000000000005, 0.312, 0.23695999999999998, 0.21018000000000003, 0.12947999999999998, 0.06984]

#REVENUES
Maxime = [0.9949465858255697, 0.9198935824839911, 0.8525311170399699, 0.8443881634392039, 0.805311254649213, 0.849549979044809]
Nrpa_c = [1.5029713049302043, 1.4930727376990085, 1.4781940042790065, 1.4486597263460521, 1.3772062760581267, 1.4093150788134803]
Nrpa = [0.7277797795580058, 0.08843161515715807, 0.0, 0.0, 0.0, 0.0]
Nepa_c = [1.4951261546357233, 1.4798327027340665, 1.4826654721255463, 1.4456845989471243, 1.3952683106107628, 1.3851398581035543]
'''

#Résultats graphe complet 500 slices 6 algos """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

#************Lambda
'''
#ACCEPTANCES
Maxime =[1.0, 0.9703999999999999, 0.8892, 0.8458, 0.8, 0.7466, 0.694, 0.639, 0.622, 0.5908, 0.5448]
Nrpa   =[1.0, 0.9702000000000001, 0.8832000000000001, 0.8392000000000001, 0.792, 0.7373999999999999, 0.6884, 0.633, 0.6274, 0.587, 0.5466]
Nrpa_c =[1.0, 0.9742000000000001, 0.8914, 0.8502000000000001, 0.8084, 0.7484, 0.6978, 0.6386000000000001, 0.633, 0.5962000000000001, 0.5522]
Nepa_c=[1.0, 0.9733999999999999, 0.8936000000000001, 0.8503999999999999, 0.8036, 0.7494, 0.6996, 0.641, 0.629, 0.5896, 0.555]

#REVENUES
Maxime=[1.526812088768556, 1.439881144466129, 1.359878144663163, 1.3374343012733385, 1.317354713298187, 1.304559650337034, 1.296743426024305, 1.2923154702869897, 1.2784727879775908, 1.2714344687777426, 1.2756161669297128]
Nrpa=[1.0073264438111962, 1.006881988500351, 1.0064019653149605, 1.0068137177308867, 1.006508719777273, 1.0076953116163856, 1.0073669420009197, 1.007380496660888, 1.00646334800884, 1.0068283854978934, 1.006949219355891]
Nrpa_c=[1.2502987019133127, 1.2481672803178057, 1.2536427350287829, 1.2500217119029846, 1.2551438887979594, 1.2524686215000507, 1.2544897019174015, 1.2529138011139478, 1.2551917184503076, 1.2509172872991126, 1.2473877198494585]
Nepa_c =[1.1036240060167601, 1.1059245718490431, 1.1049078285606497, 1.1060504182633166, 1.1053391995552126, 1.1051494817381002, 1.1062374449369954, 1.102995474217762, 1.107172660922456, 1.1059005015711079, 1.1053226024832747]

************ Slice
Maxime =[1.0, 1.0, 0.9926, 0.9773999999999999, 0.9748, 0.9592, 0.9454, 0.9178, 0.9054, 0.865]
Nrpa   =[1.0, 1.0, 0.9922000000000001, 0.9756, 0.9722000000000001, 0.9558, 0.9416, 0.9144, 0.9017999999999999, 0.8617999999999999]
Nrpa_c =[1.0, 1.0, 0.9942000000000001, 0.979, 0.9778, 0.9626, 0.9484, 0.9148, 0.8904, 0.8596]
Nepa_c= [1.0, 1.0, 0.994, 0.98, 0.9773999999999999, 0.9608, 0.9486, 0.917, 0.8907999999999999, 0.8654]
#REVENEUS
Maxime=[1.4861432114511277, 1.4374620963483848, 1.3983495429247266, 1.3336305761505167, 1.3137509447282016, 1.2871935894025475, 1.264425913462565, 1.2261410719461767, 1.2099062827067404, 1.192791962711438]
Nrpa=  [1.007076163546404, 1.0069564553492252, 1.0071180270870395, 1.0064866020735095, 1.006252344877401, 1.00621125796305, 1.0066372413020077, 1.0059762139204698, 1.0060949764162717, 1.0059238998037423]
Nrpa_c=[1.2294885606302348, 1.2037214383352577, 1.1879630365203042, 1.1648399207567555, 1.1502369644109176, 1.139328487690848, 1.127647734159968, 1.1118574825727547, 1.1009543461773248, 1.0900963457067887]
Nepa_c=[1.1020443580910517, 1.095198881105371, 1.0907550916002546, 1.0848046877761015, 1.0825708487563808, 1.0792997126302963, 1.0756013367797475, 1.071596599598063, 1.066528246802833, 1.0634813597703017] 

*********** Physical
Maxime =[0.6512000000000001, 0.7293999999999999, 0.7542000000000001, 0.804, 0.8335999999999999, 0.8419999999999999]
Nrpa   =[0.6482, 0.7266000000000001, 0.7515999999999999, 0.7973999999999999, 0.8259999999999998, 0.8393999999999997]
Nrpa_c =[0.6628, 0.7358000000000001, 0.7626000000000001, 0.8049999999999999, 0.8388, 0.8507999999999998]
Nepa_c=[0.657, 0.7355999999999999, 0.7542000000000001, 0.8074000000000001, 0.8413999999999999, 0.8468]
#REVENEUS
Maxime=[1.3277561563861107, 1.2811707552939142, 1.2562200937774504, 1.237639993141583, 1.2268684275917978, 1.2125346891997146]
Nrpa = [1.0101483646752174, 1.0086643092445164, 1.0066210185761018, 1.0060597709156787, 1.0055849820599876, 1.0046633684512636]
Nrpa_c=[1.2850769178807773, 1.2434752978059975, 1.203699562926474, 1.1815508531663605, 1.1558817178011276, 1.137369639238132]
Nepa_c=[1.1288106112848406, 1.1146120660658487, 1.0969754199066897, 1.0855230540067533, 1.078184336758863, 1.068906904433334]

################### BW
#ACCEPTANCES

Maxime =[0.9997999999999999, 0.9996, 1.0, 1.0, 0.9994, 1.0]
Nrpa   =[0.375, 0.6162000000000001, 0.86, 0.9716, 0.9972000000000001, 0.9986]
Nrpa_c =[0.9982000000000001, 0.9984, 1.0, 1.0, 0.9992000000000001, 0.999]
Nepa_c =[0.9977999999999999, 0.999, 1.0, 1.0, 1.0, 0.9997999999999999]

#REVENUE
Maxime=[1.4027253425824857, 1.415106696166704, 1.4389289756367478, 1.459716897231926, 1.460637324699141, 1.4776291751778425]
Nrpa = [1.0058030577718795, 1.0051921991611197, 1.0052933378677287, 1.0055676817720605, 1.006163472446477, 1.0063880112999617]
Nrpa_c =[1.311332826827828, 1.2971256083136269, 1.2898410654587766, 1.283294726277026, 1.274214460824498, 1.2707845913444962]
Nepa_c =[1.2067122162689583, 1.185420437986766, 1.1672587955675988, 1.1538971610138982, 1.133102724086776, 1.123574259439448]

################CPU
#ACCEPTANCES

Maxime =[0.6242000000000001, 0.7747999999999999, 0.8413999999999999, 0.9306, 0.961, 0.9768]
Nrpa   =[0.6174, 0.7694, 0.8288, 0.9246, 0.9568, 0.9768]
Nrpa_c =[0.6214, 0.7746000000000001, 0.8356, 0.9298, 0.9604, 0.978]
Nepa_c = [0.6312000000000001, 0.7836000000000001, 0.848, 0.9342, 0.9636, 0.9772000000000001]

#REVENUES
Maxime=[1.179384454168865, 1.2096927072918187, 1.2418176728428352, 1.2944039981924815, 1.3271804400051441, 1.360312924754723]
Nrpa=  [1.005066536105732, 1.0057617053221872, 1.0059459650425753, 1.0060408647260646, 1.0065145462352683, 1.0064978516549137]
Nrpa_c=[1.181610015821939, 1.1988160130095564, 1.2108045193258234, 1.2299406578778243, 1.242678591717879, 1.2468636242761046]
Nepa_c=[1.0740299926324082, 1.0801024574714777, 1.085395371062704, 1.0913456836152216, 1.0947459288613544, 1.0963408120287927]

###################"Ressources
#ACCEPTANCES

Maxime =[0.5776, 0.763, 0.8262, 0.9184, 0.9458, 0.9828]
Nrpa   =[0.3282, 0.6038, 0.7637999999999999, 0.8964, 0.9404, 0.9818]
Nrpa_c =[0.5562, 0.7482000000000001, 0.8182, 0.9146, 0.9456, 0.9813999999999999]
Nepa_c =[0.575, 0.7682, 0.8322, 0.9196, 0.9498, 0.9836]

#REVENUES
Maxime =[1.1043334761155348, 1.1481992366064162, 1.1740885219529864, 1.2379883026908547, 1.2720561317386816, 1.3529104329418182]
Nrpa   =[1.0035708748975771, 1.0032516424014113, 1.0040054534266425, 1.005232992796469, 1.0060132103172676, 1.006286201165179]
Nrpa_c =[1.1840324738189945, 1.2028438376327766, 1.2132105582562793, 1.234574248975968, 1.2349963903139325, 1.2502231993562338]
Nepa_c =[1.108106411282614, 1.111112371008775, 1.1138443292036047, 1.1177749965784707, 1.1142281789447153, 1.1134127734424262]
'''


''' #RUNTIME ******************************************************************************
# Données
algorithms = [ 'NEPA(path)', 'NEPA-DLPlus', 'NRPA-DL', 'NRPA-DLPlus']
runtimes = [0.4567615895895636, 0.37110030907629094, 0.3574469684108364,  0.2832534573542909]  # Temps d'exécution (en secondes)
#sliceSize [0.6778270569402182, 0.5654489918248363, 0.4641672794412183, 0.47651698765285455]

# Création du graphique en barres horizontales
fig, ax = plt.subplots(figsize=(8, 4))  # Taille plus grande pour plus de clarté

y_pos = np.arange(len(algorithms))

# Amélioration des couleurs avec une palette plus douce et des bordures autour des barres
bars = ax.barh(y_pos, runtimes, color='steelblue', edgecolor='black')

# Ajout des étiquettes
ax.set_yticks(y_pos)
ax.set_yticklabels(algorithms, fontsize=12)
ax.invert_yaxis()  # Le premier en haut

# Ajouter un titre et une légende des axes
ax.set_xlabel('Runtime per slice (seconds)', fontsize=12)

# Ajouter des annotations pour chaque barre (afficher la valeur)
for bar in bars:
    width = bar.get_width()
    ax.text(width + 0.02, bar.get_y() + bar.get_height()/2, 
            f'{width:.2f}', va='center', ha='left', fontsize=10)

# Ajuster les limites de l'axe X
ax.set_xlim([0, 1])

# Supprimer les bordures autour du graphique
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Ajouter un peu d'espace autour du graphique
plt.tight_layout()

# Affichage du graphique
plt.show()
'''


''' #Saturation & ECDF ***************************************************************************************
# Saturation CPU du SN
variable = np.linspace(1, 100, num=100)  # Génère les valeurs de 1 à 100 pour l'axe des X

bw_base = [2.218430034129693, 5.597269624573379, 7.440273037542662, 5.597269624573379, 7.815699658703072, 4.436860068259386, 2.218430034129693, 5.699658703071672, 6.962457337883959, 9.283276450511945, 8.020477815699659, 11.774744027303754, 8.293515358361775, 10.511945392491468, 10.511945392491468, 10.511945392491468, 8.19112627986348, 8.19112627986348, 8.19112627986348, 18.907849829351537, 18.907849829351537, 18.907849829351537, 18.907849829351537, 18.907849829351537, 16.68941979522184, 16.68941979522184, 16.68941979522184, 14.47098976109215, 14.47098976109215, 18.63481228668942, 18.63481228668942, 7.918088737201365, 12.832764505119455, 27.986348122866893, 24.2320819112628, 19.31740614334471, 19.31740614334471, 25.187713310580204, 21.023890784982935, 27.918088737201366, 27.918088737201366, 27.918088737201366, 12.764505119453926, 12.764505119453926, 14.709897610921502, 14.709897610921502, 14.709897610921502, 14.709897610921502, 12.764505119453926, 12.764505119453926, 12.764505119453926, 12.764505119453926, 12.764505119453926, 12.764505119453926, 12.764505119453926, 12.764505119453926, 12.764505119453926, 12.764505119453926, 12.764505119453926, 6.8941979522184305, 6.8941979522184305, 6.8941979522184305, 7.030716723549488, 9.215017064846416, 12.832764505119455, 12.832764505119455, 12.696245733788396, 12.901023890784982, 12.901023890784982, 12.901023890784982, 10.716723549488055, 7.098976109215017, 6.8941979522184305, 15.972696245733788, 15.972696245733788, 15.972696245733788, 15.972696245733788, 15.972696245733788, 15.972696245733788, 15.972696245733788, 15.972696245733788, 15.972696245733788, 9.078498293515358, 11.774744027303754, 11.774744027303754, 11.774744027303754, 11.774744027303754, 11.774744027303754, 11.774744027303754, 11.774744027303754, 11.774744027303754, 11.774744027303754, 11.774744027303754, 11.774744027303754, 11.774744027303754, 11.774744027303754, 11.774744027303754, 2.696245733788396, 0.0, 0.0]
bw_pred = [2.1160409556313993, 5.1194539249146755, 7.5426621160409555, 5.1194539249146755, 6.040955631399317, 3.037542662116041, 2.1160409556313993, 4.709897610921502, 6.450511945392491, 8.703071672354948, 6.962457337883959, 11.945392491467576, 9.351535836177474, 10.955631399317406, 10.955631399317406, 10.955631399317406, 8.703071672354948, 8.703071672354948, 8.703071672354948, 8.703071672354948, 10.887372013651877, 10.887372013651877, 10.887372013651877, 10.887372013651877, 9.283276450511945, 12.35494880546075, 12.35494880546075, 10.238907849829351, 8.054607508532424, 14.53924914675768, 14.53924914675768, 14.53924914675768, 14.53924914675768, 19.488054607508534, 14.505119453924914, 14.505119453924914, 14.505119453924914, 14.505119453924914, 8.020477815699659, 17.542662116040955, 17.542662116040955, 17.542662116040955, 12.593856655290102, 12.593856655290102, 14.53924914675768, 14.53924914675768, 14.53924914675768, 14.53924914675768, 12.593856655290102, 17.372013651877133, 12.593856655290102, 12.593856655290102, 12.593856655290102, 12.593856655290102, 12.593856655290102, 9.522184300341298, 22.764505119453926, 22.764505119453926, 22.764505119453926, 22.764505119453926, 22.764505119453926, 9.522184300341298, 9.658703071672354, 11.604095563139932, 14.095563139931741, 14.095563139931741, 13.959044368600683, 16.07508532423208, 16.07508532423208, 16.07508532423208, 14.129692832764505, 11.638225255972696, 9.522184300341298, 18.907849829351537, 18.907849829351537, 18.907849829351537, 18.907849829351537, 18.907849829351537, 18.907849829351537, 18.907849829351537, 18.907849829351537, 18.907849829351537, 9.38566552901024, 12.081911262798634, 12.081911262798634, 12.081911262798634, 12.081911262798634, 21.74061433447099, 21.74061433447099, 21.74061433447099, 21.74061433447099, 21.74061433447099, 21.74061433447099, 12.081911262798634, 12.081911262798634, 12.081911262798634, 12.081911262798634, 2.696245733788396, 0.0, 0.0]

cpu_base = [
    15.96, 43.97, 69.95, 43.97, 63.53, 35.52, 15.96, 42.87, 61.50, 79.34, 60.71, 86.38,
    59.46, 75.89, 75.89, 75.89, 58.05, 58.05, 58.05, 92.48, 92.48, 92.48, 92.48, 92.48,
    76.05, 76.05, 76.05, 60.09, 60.09, 84.03, 84.03, 49.60, 74.33, 92.64, 66.97, 42.25,
    42.25, 69.01, 45.07, 83.88, 83.88, 83.88, 65.57, 65.57, 83.72, 83.72, 83.72, 83.72,
    65.57, 65.57, 65.57, 65.57, 65.57, 65.57, 65.57, 65.57, 65.57, 65.57, 65.57, 38.81,
    38.81, 38.81, 52.11, 68.54, 82.00, 82.00, 68.70, 86.54, 86.54, 86.54, 70.10, 56.65,
    38.81, 79.34, 79.34, 79.34, 79.34, 79.34, 79.34, 79.34, 79.34, 79.34, 40.53, 64.94,
    64.94, 64.94, 64.94, 64.94, 64.94, 64.94, 64.94, 64.94, 64.94, 64.94, 64.94, 64.94,
    64.94, 64.94, 24.41, 0.0
]

cpu_pred = [
    15.96, 43.97, 69.95, 43.97, 63.53, 35.52, 15.96, 42.87, 61.50, 79.34, 60.71, 86.38,
    59.46, 75.89, 75.89, 75.89, 58.05, 58.05, 58.05, 58.05, 79.49, 79.49, 79.49, 79.49,
    63.06, 85.28, 85.28, 69.32, 47.88, 71.83, 71.83, 71.83, 71.83, 90.14, 64.47, 64.47,
    64.47, 64.47, 40.53, 79.34, 79.34, 79.34, 61.03, 61.03, 79.18, 79.18, 79.18, 79.18,
    61.03, 88.10, 61.03, 61.03, 61.03, 61.03, 61.03, 38.81, 71.51, 71.51, 71.51, 71.51,
    71.51, 38.81, 52.11, 68.54, 82.00, 82.00, 68.70, 86.54, 86.54, 86.54, 70.10, 56.65,
    38.81, 79.34, 79.34, 79.34, 79.34, 79.34, 79.34, 79.34, 79.34, 79.34, 40.53, 64.94,
    64.94, 64.94, 64.94, 89.98, 89.98, 89.98, 89.98, 89.98, 89.98, 64.94, 64.94, 64.94,
    64.94, 24.41, 0.0, 0.0
]

# Tracer les deux courbes de saturation du CPU
plt.figure(figsize=(10, 6))

plt.plot(variable, cpu_pred, label='NRPA Prediction', color='green')
plt.plot(variable, cpu_base, label='NRPA', color='blue')


# Configurations du graphique
plt.xlabel('Arrival & Departure of Slices')
plt.ylabel('CPU Saturation (%)')
plt.title('Comparison of CPU Resource Saturation: NRPA vs NRPA Prediction')
plt.grid(True)
plt.legend()

# Afficher le graphique
plt.show()

#ECDF
variable = np.linspace(1, 50, num=50)  # Génère les valeurs de 1 à 50 pour l'axe des X

ecdf_pred=[1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9, 9, 9, 10, 10, 10, 10, 11, 12, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 16, 17, 17, 18, 19, 20, 20, 21, 21, 22, 22, 22, 22, 22, 22, 23, 23, 23, 24, 24, 24]
ecdf_base=[1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 11, 11, 12, 13, 14, 15, 15, 16, 16, 16, 16, 16, 16, 16, 17, 18, 19, 19, 20, 20, 21, 21, 21, 21, 21, 21, 22, 22, 22, 22, 22, 22]
#ecdf_sorted = np.sort(ecdf)  # Trier les données
#y_values = np.arange(1, len(ecdf_sorted) + 1) / len(ecdf_sorted)  # Calculer la proportion cumulée

plt.figure(figsize=(8, 6))
plt.step(variable, ecdf_pred, where='post', label='NRPA Prediction', color='blue')
plt.step(variable, ecdf_base, where='post', label='NRPA', color='gray')
plt.xlabel('Arrival slices')
plt.ylabel('Sum of acceptance')
plt.title('Empirical Cumulative Distribution Function (ECDF)')
plt.grid(True)
plt.legend()
plt.show()
'''


