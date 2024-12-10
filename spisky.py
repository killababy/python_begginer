names = ["Sonya", "Valeriya", "Evgeniya", "Marina", "Aleksandr"]
print(names[0]) #Вывод первого имени в списке
print(names[-1]) #Вывод первого имени с конца списка в списке
print(names[2].lower()) #Вывод третьего имени в нижнем регистре
print(names[-2].upper()) #Вывод второго имени с конца списка в верхнем регистре
message = f"{names[0].title()} is my best friend!"
print(message)
message2 = f"My older brother's name is {names[-1]}."
print(message2)
bts_names = ["Jin", "V", "Jung Kook", "Suga", "J-Hope", "RM", "Jimin"]
bts_favorite_idol_message = f"My favorite IDOL from BTS is {bts_names[-3]}"
bts_cutest_idol_message = f"In my opinion, the cutest IDOL from BTS is {bts_names[-1]}"
bts_handsome_idol_message = f"In my opinion, the handsome IDOL from BTS is {bts_names[0]}"
bts_younger_idol_message = f"The youngest member of BTS is {bts_names[2]}"
bts_leader_message = f"The leader of BTS is {bts_names[-2]}"
bts_kindest_idol_message = f"In my opinion,the kindest member of BTS is {bts_names[1]}"
bts_best_rapper_message = f"In my opinion, the coolest rapper in BTS is {bts_names[3]}"
print(bts_favorite_idol_message,"\n", bts_cutest_idol_message,"\n",bts_handsome_idol_message,"\n",bts_younger_idol_message,"\n",bts_leader_message,"\n",bts_kindest_idol_message,"\n",bts_best_rapper_message)