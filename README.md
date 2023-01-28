# Mpesa_Statement_Analysis
So I started working on it around the first weeks of December 2022, definitely started with a lot of expectations. Thought this would be like a one week project and I’d be done, but life hit me with the, “You thought I was feeling you? ha!” Second week of December we had a class trip to Msa and final year project presentations, Third week, we had our final exams and well 4th week is Christmas.

So I started the project again this January, around 3rd, but you know I just finished school, I was super focused on landing a job by the end of January. Life still hitting me with the, you thought I was feeling you😂😂……. anyway, I got back to the project. I gave up on the 5th! “Why?” I bet that’s your question. 


### **Data Cleaning**

Well you see our mpesa transactions are saved as they are. Not in a way that saves you the job of data cleaning. Imagine going through 9876 rows of data, one row at a time with your mpesa statement next to it, trying to imagine what exactly you were paying for in that Till Number! Those were the struggles. I’d find myself paying over 800 bob to a till number but no record of what I was paying for!!!!!!!! How do I keep track of my expenses without the proof of what you were purchasing. So I gave up. I wasn’t going to clean all those rows on my own. Who me! Never!

Well I did clean the 9876 rows, I sat down everyday for 30 minutes right before bed, opened my original mpesa statement, opened the 2022 calender, went through my chats with friends to try and find if I said something to them about going shopping, or going out. Good thing about me, I have a box of most of the receipts I get after shopping, it helps me keep count of my reward points. 10 days later, I was done with renaming the rows, Lemme show you a sneak peek:

I took it from this;


![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/5jg4dso06ooard5wmf9q.png)

to this

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/c7ek6kq1qnkpcykwigti.png)

### **Working on the Data**

After cleaning, well I had the statement in the format that I wanted. It’s like finishing the dirty job of cleaning squids but now you’re done and can easily cook them in accordance to your recipe. Onto the next task, well I didn’t need the time column honestly. So I dropped it. That was actually the 1st and only thing I dropped on the entire dataset. Safaricom’s data team is doing a good job keeping their data quite easy to work with. Next step, extracting months from the date column. That’s an easy task right! After that I just had to do some analysis on the data, if you notice the workbook names at the bottom of my excel screenshots, well you can see the kind of work I did.
By 20th of January, I had calculated my monthly expenses, income, read a lot of money books about what situation 21-year old me is in, financially. Back to the interesting stuff, 21 pivot tables later, I actually stayed working on the dashboard, but….. it just didn’t click to me. The plots, analysis, tables, all of that was okay I just didn’t like the design. Tell me if I’m wrong... this is what it looked like. 
![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/yanymt6n1ocnr3mrbwgu.png)
