# Sherman - yet another stock bot


## Instructions for Sherman:

  1. Go to: https://alpaca.markets to create an account
  

  2. Go into your terminal and type: "pip install alpaca-trade-api"


  3. Copy and paste the code into your text editor, notepad, etc.


  4. Log into you account on Alpaca, and click on the View button next to the text that says: "Your API keys"


  5. Take the key and paste it into the quotes in the code that says "my_key", do the same for your secret key with "my_sec_key".


  6. Change the "symbol" variable in the code from "AAPL" to whatever stock you would like to trade with.


  7. Change the "qty" variable in the code to how much you would like to buy and sell of your stock.


  8. Create a .txt file named "updates" in the same directory of file you saved your code in.


  9. In the "position" variable change "AAPL" to your stock name.


  10. 

  In the line that says `if percent_change >= 0.5 and int(position.qty) == 501:` change `0.5` to the percent you would like to buy and sell at, and `501` to your qty + 1. 
  In the line that says `elif percent_change <= -0.5 and int(position.qty) == 1:` change `-0.5` to what you changed `0.5` above but negative.


  11. In this snippet of code:
  
    update1.write("\n" + time1 + f": Sherman bought 500 shares of " + symbol + " for {minute_open} each.")
        update1.close()

        print(f"Sherman bought 500 shares of " + symbol + " for {minute_open} each.")
         
   
   Change `500` to the qty you are buying and selling, you need to do this twice since there is an if statement with this, and an elif statement as well.


  12. And you should be all set just run the script.
  
  
  
### Instructions for MSherman:
  
  Basically the same thing as above just change the stockname variables to your stocks, the stockqty to the qty of your stocks, and the percent to the eprcent you want.
