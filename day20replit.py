start = int(input("List your starting number: "))
end = int(input("List your ending number: "))
increments = int(input("List what you'd like to count by: "))
list = 0
for list in range(start,end,increments):
    print(list)
