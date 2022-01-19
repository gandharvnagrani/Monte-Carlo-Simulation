Python 3.9.2 (v3.9.2:1a79785e3e, Feb 19 2021, 09:06:10) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> def monte_carlo(start_price, days, sigma, mu): #note that we have already defined dt as 1/days
    ''' (float, int, float, float) -> array
    This function takes in starting stock price, days of simulation,mu,sigma, and returns simulated price array'''
    #Initialize a price array
    price = np.zeros(days)
    price[0] = start_price
    
    #Initialize arrays for shock and drift values
    shock = np.zeros(days)
    drift = np.zeros(days)
    
    #Run price array for number of days:
    for x in range(1,days):
        shock[x] = np.random.normal(loc = mu*dt, scale = sigma*np.sqrt(dt)) 
        #center this array around the mean, set the scale as the std deviation times dt
        drift[x] = mu*dt #check the formula above
        price[x] = price[x-1] + (price[x-1]*(shock[x]+drift[x]))
        #This equation makes sense because the price of the current stock is equal to the value of the previous stock + the change (delta s)
        
    return price