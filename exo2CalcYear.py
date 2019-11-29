nsd = 1234567892
t = 0

secondes = nsd % 60
t = nsd // 60
minutes = t % 60
t = nsd // 60
heures = t % 24
t = nsd // 24
jour = t % 30
t = nsd // 30
mois = t % 365
t = nsd // 365
annees = t


print(secondes)
print(minutes)
print(heures, ':' ,minutes, ':', secondes)
print(jour)
print(mois)
print(annees)