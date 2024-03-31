import math

arr = {
    "anchorage": {
        "dd": [-149.9002, 61.2181, 22]
    },
    "los_angeles": {
        "dd": [-118.2437, 34.0522],
    }
}
dd = [-118.2437, 34.0522]
wOrN = ["w", "n"]
dms = []
for i in arr.keys():
    print(i)
    for j in arr[i].values():
      for n in range(j.__len__):
       print(j[n])
def loop_over_dd():
  for x in range(2):
    print(x)
    convert_to_dms_degrees(x)
    if dd.__len__() == 3:
     dms.append(dd[dd.__len__()-1])
  print (dms)

def convert_to_dms_degrees(x):
 tmpdms = []
 before_floote = abs(dd[x])
 frac, whole = math.modf(before_floote)
 tmpdms.append(whole)
 for y in range(2):
  before_floote = frac*60
  frac,whole = math.modf(before_floote)
  tmpdms.append(before_floote)
 tmpdms.append(wOrN[x]) 
 dms.append(tmpdms)
loop_over_dd()
