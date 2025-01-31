

data = """
- physical 100_0
428,1.1379775804254384,290.019731792
424,1.1369159781947713,290.985761236
423,1.135399822317589,289.40800241
429,1.1396780869180339,290.92581326
425,1.1418075838497397,289.071283616
424,1.1350954863957003,287.980521744
424,1.1378636678255332,290.431417757
425,1.1355009726106342,290.079528394
425,1.1364078142510254,286.814658924
427,1.137049399592855,288.990274553
- physical 100_1
428,1.1379775804254384,292.280825128
424,1.1369159781947713,290.203120196
423,1.135399822317589,289.011231727
429,1.1396780869180339,291.466168475
425,1.1418075838497397,287.540241108
424,1.1350954863957003,288.20207032
424,1.1378636678255332,288.198080312
425,1.1355009726106342,292.041799958
425,1.1364078142510254,284.329038751
427,1.137049399592855,289.367672003
- physical 100_2
428,1.1379775804254384,290.471540248
424,1.1369159781947713,290.981280559
423,1.135399822317589,289.97890263
429,1.1396780869180339,291.567055069
425,1.1418075838497397,290.51714531
424,1.1350954863957003,288.293839624
424,1.1378636678255332,290.383873786
425,1.1355009726106342,291.725300559
425,1.1364078142510254,285.030853359
427,1.137049399592855,289.353722715
- physical 100_3
428,1.1379775804254384,290.435694798
424,1.1369159781947713,292.923355308
423,1.135399822317589,290.406718711
429,1.1396780869180339,289.200062336
425,1.1418075838497397,288.993699077
424,1.1350954863957003,288.872406744
424,1.1378636678255332,288.904463086
425,1.1355009726106342,290.269936093
425,1.1364078142510254,284.312907526
427,1.137049399592855,288.364611682
- physical 100_4
428,1.1379775804254384,291.212364029
424,1.1369159781947713,291.22622629
423,1.135399822317589,288.585619956
429,1.1396780869180339,290.380058871
425,1.1418075838497397,289.488739745
424,1.1350954863957003,288.283361646
424,1.1378636678255332,288.239443779
425,1.1355009726106342,291.122366564
425,1.1364078142510254,284.357891202
427,1.137049399592855,289.649393583
- physical 100_5
428,1.1379775804254384,291.356774353
424,1.1369159781947713,290.601097488
423,1.135399822317589,290.172965623
429,1.1396780869180339,290.605694966
425,1.1418075838497397,289.011459882
424,1.1350954863957003,289.486157802
424,1.1378636678255332,288.944404577
425,1.1355009726106342,289.582041952
425,1.1364078142510254,285.017071495
427,1.137049399592855,289.484952882
- physical 100_6
428,1.1379775804254384,291.680648843
424,1.1369159781947713,292.682536831
423,1.135399822317589,289.076089254
429,1.1396780869180339,290.836309144
425,1.1418075838497397,287.793061711
424,1.1350954863957003,288.723198599
424,1.1378636678255332,289.650871695
425,1.1355009726106342,290.557981889
425,1.1364078142510254,284.66614266
427,1.137049399592855,289.099965232
- physical 100_7
428,1.1379775804254384,290.370108875
424,1.1369159781947713,292.411637754
423,1.135399822317589,289.663682991
429,1.1396780869180339,291.963401227
425,1.1418075838497397,290.72426436
424,1.1350954863957003,287.996899823
424,1.1378636678255332,288.98440668
425,1.1355009726106342,290.656324258
425,1.1364078142510254,286.022761547
427,1.137049399592855,288.62037967
- physical 100_8
428,1.1379775804254384,290.441494561
424,1.1369159781947713,290.564744889
423,1.135399822317589,291.403617908
429,1.1396780869180339,291.532580674
425,1.1418075838497397,289.50057925
424,1.1350954863957003,288.705133713
424,1.1378636678255332,289.229742241
425,1.1355009726106342,290.221925157
425,1.1364078142510254,285.504346299
427,1.137049399592855,289.126174203
- physical 100_9
428,1.1379775804254384,288.196915345
424,1.1369159781947713,289.816409997
423,1.135399822317589,289.473791227
429,1.1396780869180339,289.555852084
425,1.1418075838497397,288.868674935
424,1.1350954863957003,288.76485563
424,1.1378636678255332,289.18196365
425,1.1355009726106342,291.125499621
425,1.1364078142510254,285.585764063
427,1.137049399592855,290.021110206
"""



sections = data.strip().split("- physical")
acceptances=[]
revenues=[]

for section in sections[1:]:
    lines = section.strip().split("\n")[1:]  
    acceptancesS = 0
    revenuesS = 0

    for i, line in enumerate(lines):
        values = line.split(",")
        acceptance = float(values[0])
        if values[1] == 'NaN':
            values[1] = 0
        revenue = float(values[1])
        runtime = float(values[2])
        
        acceptancesS += acceptance


    acceptances.append((acceptancesS / 10) / 500)
    revenues.append(revenuesS / 10)


#acceptances.reverse() #if ressources use this ! 
#revenues.reverse() #if ressources use this !

#for physical use this !
nbr=len(acceptances)
somme=sum(acceptances)
moyenne=somme/nbr 
print(moyenne)
nb=len(revenues)
som=sum(revenues)
rev=som/nb
print(rev)
'''
#print(acceptances)
#print(revenues)
'''
