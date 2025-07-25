select * from zomato1;

#Where Between  Function 
select * from zomato1 where Price between 100 and 300;

#Where in Function 
select* from zomato1 where price IN (99,199);

select * from zomato1 where Category="Veg";

select * from zomato1 where Category="Veg" and Member="Harshini";

#where with date 
select * from zomato1 where date="20-03-2025";

select * from zomato1 where Date>'01-01-2025';

select * from zomato1 where date>'01-01-2025' and date<'01-04-2025';

#where not function 
select * from zomato1 where not price="168";

#Like Fucntion 
select * from zomato1 where Dishname like "Chicken%"; #name starts with 

#name ends with
select * from zomato1 where Dishname regexp "Biriyani$";

#like or function 
select * from zomato1  where date regexp "-02-|-04";

#Update Function 
select * from zomato1;
UPDATE zomato1
SET Price = 200
WHERE Category = 'Veg' AND Member = 'Harshini';


#Insert Function
select * from zomato1;
INSERT INTO zomato1 (Dishname, Price, Category, Member, Date)
VALUES ('Butter Chicken', 280, 'Non-Veg', 'Rahul', '2025-03-20');

#Delete Function 
select * from zomato1;
DELETE FROM zomato1 WHERE Member = 'Rahul';


#Create and insert Table Function
INSERT INTO zomato1 (Dishname, Price, Category, Member, Date)
VALUES 
('Paneer Butter Masala', 220, 'Veg', 'Harshini', '2025-03-20'),
('Chicken Biryani', 280, 'Non-Veg', 'Rahul', '2025-03-21'),
('Veg Fried Rice', 150, 'Veg', 'Harshini', '2025-03-22'),
('Mutton Rogan Josh', 350, 'Non-Veg', 'Arjun', '2025-03-23'),
('Gobi Manchurian', 130, 'Veg', 'Deepa', '2025-03-24'),
('Fish Curry', 300, 'Non-Veg', 'Harshini', '2025-03-25'),
('Dal Tadka', 140, 'Veg', 'Vikram', '2025-03-26'),
('Chicken 65', 200, 'Non-Veg', 'Nisha', '2025-03-27'),
('Chole Bhature', 160, 'Veg', 'Harshini', '2025-03-28'),
('Egg Curry', 180, 'Non-Veg', 'Rahul', '2025-03-29');

select * from zomato1;

#Count Function 
SELECT COUNT(*) FROM zomato1;

#Average and Groupby
SELECT Category, AVG(Price) AS AvgPrice FROM zomato1 GROUP BY Category;

#Minimum and Maximum 
SELECT MAX(Price), MIN(Price) FROM zomato1;


#Orderby Function 
SELECT * FROM zomato1 ORDER BY Price DESC LIMIT 5;


#Orderby month or date
SELECT MONTH(Date) AS Month, COUNT(*) AS TotalOrders
FROM zomato1
GROUP BY MONTH(Date);

#Sum ad Revenue
SELECT MONTH(Date) AS Month, SUM(Price) AS Revenue
FROM zomato1
GROUP BY MONTH(Date);


#Data Modification 
UPDATE zomato1
SET Price = Price * 1.1
WHERE Category = 'Non-Veg';

select * from zomato1;