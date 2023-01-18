from read_data import read_data

def find_all_users_id(data: dict)->list:
    """ 
    This function will find all the users in the json file and return the list of users id
    
    Parameters:
        data (dict): Dictionary containing the data of the json file
    Returns:
        list: List containing all the users id
    """
    messages=data['messages']
    user_id=[]
    for i in messages:
        actor_id=i.get('actor_id')
        from_id=i.get('from_id')

        if from_id!=None:
            is_channel='channel' in from_id

            if not from_id in user_id and not is_channel:
                user_id.append(from_id)
        else:
            is_channel='channel' in actor_id

            if not actor_id in user_id and not is_channel:
                user_id.append(actor_id)


    return user_id
x=read_data('data/result.json')
print(find_all_users_id(x))