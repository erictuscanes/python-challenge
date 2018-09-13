import csv
with open('budget_data.csv') as csvfile:
    
    for row in csvfile:
        total_months = 0
        net_amount = str(0)
        average = 0
       
        total_months = (row[0] +1)
        net_amount = sum(row[1])
        average = (net_amount) / (total_months)
        biggest_gain = max(row[1])
        biggest_loss = min(row[1])
        
        print("Total months": {str(total_months)})
        print("Total": {str(net_aoun)})
        print("Average change": {str(average)})
        print("Greatest Increase in Profits": {str(drawPercent)})
        print("Greatest Decrease in Profits": {str(biggest_loss)})
        
import python as /path/to/script/main.py > /path/to/output/myfile.txt 
