from covid import Covid
import matplotlib.pyplot as pyplot
country=input("Enter your country name:")
covid=Covid()
data=covid.get_status_by_country_name(country)
'''
for eg. data={'id': '27', 'country': 'India', 'confirmed': 490401, 'active': 189463, 'deaths': 15301, 'recovered': 285637,
'latitude': 20.593684, 'longitude': 78.96288, 'last_update': 1593146023000}
'''
cadr={ key:data[key]
       for key in data.keys() & {"confirmed","active","deaths","recovered"}
      }
n=list(cadr.keys())
v=list(cadr.values())
print(cadr)
#to draw the graph
pyplot.title(country)
pyplot.bar(n,v)
pyplot.show()
