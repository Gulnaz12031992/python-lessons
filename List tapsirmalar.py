# -*- coding: utf-8 -*-
"""
Created on Tue Jul 29 07:55:10 2025

@author: Admin
"""

# ismlar=['Lapiza','Malika','Feruza','Janat','Gulnaz']
# print(ismlar[0].upper())
# print(ismlar[0], 'bugin magazinge bardinba?')
# print(ismlar[1],'tayrlioq barma?',ismlar[2],'balalrin baqshadama?',ismlar[3],'nege jumista joqsan',ismlar[4],'esaplarin ornap atirma?')
# sanlar=[1,5,-7,11,45,-9]
# a=sanlar[0]+11
# b=sanlar[2]+10
# c=a+b
# d=sanlar[4]-sanlar[3]
# print(a,b,c,d)
# t_shaxslar=['al xorezmiy','beruniy','ibn sino','berdaq']
# z_shaxslar=['feruza','janat','malika']
# z_shaxslar.insert(4,'Gulnaz')
# t_shaxslar.append('Ibrayim')
# z_shaxslar.remove('malika')
# del t_shaxslar[1]
# print(t_shaxslar)
# print(z_shaxslar)
# print('men tariyxiy shaxslardan', t_shaxslar.pop(0), 'ni hurmat qilaman')
# print(z_shaxslar.pop(1),'moshniy qizgo')
# print(t_shaxslar[0].upper(),t_shaxslar[1].capitalize(),t_shaxslar[2].title())
friends=[]
friends.append('Janat')
friends.append('Malika')
friends.append('Feruza')
friends.append('Lapiza')
ky=friends.remove('Feruza')
friends.insert(0, 'Gulzar')
friends.insert(3, 'Gulshi')
friends.append('Laylo')
print(friends)
mehmonlar=[]
mehmonlar.append(friends.pop(3))
mehmonlar.append(friends.pop(2))
mehmonlar.append(friends.pop(1))
mehmonlar.append(friends.pop(0))
mehmonlar.append(friends.pop(0))
print(mehmonlar)
# ky=mehmonlar.pop(4)
# print('mehmonga kelganlar',mehmonlar,'kelmaganlar',ky)
# ismlar=['Lapiza','Malika','Feruza','Janat','Gulnaz']
# print(f'{ismlar[3]} bugin jumisqa keldinbe?,\n{ismlar[1]},bugin tayarliq boldima?,\n{ismlar[2]},balalarin baqshadama?')