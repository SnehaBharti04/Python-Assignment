import sqlite3
con=sqlite3.connect("senpai.db")
cur=con.cursor()
s="create table user2(id integer primary key autoincrement,name varchar(10),phone integer(20),email varchar(20),pass varchar(16));"
cur.execute(s)

choice=int(input("Enter \n1 New Regestration\n2 View Details\n3 Update Details\n"))

if choice==1:
	n=input("Enter Name :")
	m=input("Enter Mail :")
	ph=input("Enter Phone :")
	p=input("Enter Password :")
	
	lst=[(n,ph,m,p)]
	d="""insert into user2(name,phone,email,pass) values(?,?,?,?);"""
	cur.executemany(d,lst)
	
	print("Succccc")
elif choice==2:
	n=input("Enter Name :")
	p=input("Enter Password :")
	n="'"+n+"'"
	p="'"+p+"'"
	
	d="select * from user2 where name="+n+" and pass="+p+";"
	cur.execute(d)
	ans=cur.fetchall()
	if ans:
		print(ans)
	else:
		print("User not Exist")
elif choice==3:
	n=input("Enter Name :")
	p=input("Enter Password :")
	n="'"+n+"'"
	p="'"+p+"'"
	d="select * from user2 where name="+n+" and pass="+p+";"
	cur.execute(d)
	ans=cur.fetchall()
	
	if ans:
		x=input("Which details u want to update :")
		y=input("Enter updated detail :")
		y="'"+y+"'"
		d="update user2 set "+x+"= "+y+" where name="+n+" and pass="+p+";"
		cur.execute(d)
		print(d)
		print("Updated Successfully")
	else:
		print("User not Exist")
		

con.commit()
con.close()
