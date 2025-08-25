country_capital = {
    "India": "New Delhi",
    "Japan": "Tokyo",
    "France": "Paris",
    "USA": "Washington, D.C."
}

#telling which places and all u visited in a country
travel_log={
    "India":["Lalbagh","Museum","Planitorium"],
    "France":["Paris","Lille"],
}


#Acessing items from list
India=["Lalbagh","Museum","Planitorium"]
France=["Paris","Lille"]

print(India[2]) 

#Acessing items from dictionary- the normal one
print(country_capital["France"])

#Acessing items from dictionary- the nested one
print(travel_log["France"][1])                  #gives output = lille

#Nested list
nested_list= ['A','B',['C','D']]
print(nested_list[2][1])

#nested dictionary**********************
travel_log1={
    #Nested dictionary
    "France":{
        "cities_visited":["Paris","Lille","Dijon"],
        "num_of_times":8,
    },
    "India":{
        "cities_visited":["Bengaluru","Kerala",["Shimoga","Bidar","Bihar"]],            #nested_list
        "num_of_times":15,
    },
}

#accessing items from nested dictionary
print(travel_log1["India"])

print(travel_log1["France"]["cities_visited"][2])

print(travel_log1["India"]["cities_visited"][2])

print(travel_log1["India"]["cities_visited"][2][2])         #nested dictionary + list

