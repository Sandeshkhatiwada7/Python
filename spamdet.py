comment = input("Enter comment: ")

if ("buy now" in comment.lower() or 
   "click this" in comment.lower() or 
   "subscribe" in comment.lower() or 
   "make money" in comment.lower()):
    print("Spam detected")
else:
    print("Not spam")