def cat_dog_years(human = 1):
    
    if human == 1:
        cat,dog = 15,15        
        return human,cat,dog
    
    elif human == 2:
        cat,dog = 24,24        
        return human,cat,dog
    
    else:
        cat = 24 + ( 4 * (human - 2))
        dog = 24 + (5 * (human - 2))
        return human, cat, dog
    # else: 
    #     return "There is a error here. Please wait. "
    


print(cat_dog_years(3))