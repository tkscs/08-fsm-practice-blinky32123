# write code to implement a turnstile
current_state="locked"

while current_state!= "off":
    if current_state== "unlocked":
        print("coin has been inserted, you can walk to proceed")
    elif current_state=="locked":
        print("insert a coin to proceed")
    else:
        print(f"Error! The state {current_state} does not exist")
    the_input = input("You can input coin(coin), or push to proceed(push)\n")

    if current_state=="unlocked":
        if the_input=="coin":
           print("rejected, you have already inserted a coin")
           current_state="unlocked"
            
        if the_input=="push":
            print("spinning")
            current_state="locked" 
    if current_state=="locked":
        if the_input=="coin":
            print("unlocked")
            current_state="unlocked"
        if the_input=="push":
            current_state="locked"
            print("you must insert a coin to proceed")
            