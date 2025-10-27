import random
import time

print("🙏🌸 Swagat hai baalak! 🌸🙏")
print("✨ Tum pahunch gaye ho 'Bhavishyavani Kendra' par — jahan khud Bhagwan batayenge ki tumhare acche din kab aayenge! 😇✨\n")
time.sleep(2)
print("Bhagwan (muskurate hue): 'Bolo baccha... tumhara naam kya hai?' 😌✨\n")

# 200 random Indian names
lucky_names = [
    "Aarav","Vivaan","Reyansh","Vihaan","Aditya","Krishna","Ishaan","Arjun","Rohan","Shaurya",
    "Dev","Rudra","Kunal","Karan","Yash","Rahul","Rohit","Aryan","Kabir","Manav","Anirudh",
    "Harsh","Tanishq","Samar","Laksh","Rajat","Rishi","Ayaan","Atharv","Parth","Hriday",
    "Vikram","Nakul","Saurabh","Pranav","Tarun","Madhav","Tejas","Nirav","Amit","Chetan",
    "Siddharth","Manish","Abhay","Rajeev","Deepak","Rakesh","Akhil","Uday","Vivek","Gaurav",
    "Lumia","Aaru","Isha","Myra","Anaya","Diya","Kiara","Sara","Meera","Aarohi","Tara","Riya",
    "Naina","Sia","Avni","Aisha","Charvi","Kavya","Anika","Prisha","Mira","Tanvi","Simran",
    "Muskan","Rachita","Vani","Reeva","Navya","Ira","Suhana","Ankita","Shreya","Sneha","Pooja",
    "Ritika","Aparna","Neha","Divya","Ishita","Komal","Meghna","Payal","Kritika","Niharika",
    "Chhavi","Radhika","Bhavya","Pallavi","Rupali","Amrita","Kajal","Mahima","Anjali","Priya",
    "Aishwarya","Manisha","Smita","Surbhi","Harini","Avantika","Suhani","Bhoomi","Vaidehi",
    "Gayatri","Shraddha","Nandini","Bhawna","Kanika","Prachi","Aarushi","Sanya","Vanshika",
    "Drishti","Tanya","Juhi","Ayesha","Ashita","Chaitali","Deeksha","Ipshita","Jyoti","Mitali",
    "Sonia","Tisha","Pallavi","Preeti","Rupali","Sonali","Trisha","Urmi","Vidhi","Yamini",
    "Raj","Amitabh","Sunil","Ajay","Suresh","Kishor","Vinod","Ramesh","Anil","Deepesh","Jatin",
    "Mahesh","Vijay","Sameer","Aadesh","Ganesh","Keshav","Omkar","Pradeep","Rajesh","Santosh",
    "Lalit","Hemant","Bhaskar","Chirag","Hemesh","Dinesh","Nikhil","Ravindra","Sharad","Tushar",
    "Piyush","Bharat","Ankit","Harshit","Ravindra","Suraj","Vikash","Vimal","Prakash","Avinash",
    "Rajdeep","Harendra","Naveen","Niraj","Sanjeev","Amol","Subhash","Manoj","Satyam","Lokesh"
]

# User input
name = input("👉 Apna naam likho baalak: ").strip().capitalize()

print("\n🕉️ Bhagwan apni aankhen band karte hain... aur tumhare karmon ki file kholte hain 📜✨\n")
time.sleep(2)

if name in lucky_names:
    print(f"😇 Bhagwan (hans kar): '{name} beta! Tumhara naam to swarg ki list me likha hai sona ke aksharon me!' ✨")
    time.sleep(1)
    print("🌟 'Maze karo baalak! Tumhare acche din aa gaye hain!' 😎🌈")
else:
    print("📖 Bhagwan page palat rahe hain... dekh rahe hain... soch rahe hain... 🤔")
    time.sleep(2)
    print("🙏 'Na beta Na... Bilkul na... tumhara naam list me nahi mila!' 😅")
    time.sleep(1)
    print("😂 'Agla janam fix kar lenge... tab tak mehnat aur chai dono garam rakho!' ☕💫")

print("\n🌸 Bhagwan (muskurate hue): 'Chalo ab jao, prasadam le lo aur haste raho!' 😇🍬")
print("✨ Tumhara din shubh ho baalak! 🕉️🌼")
