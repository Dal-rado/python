def is_palindrome(s):

     s = s.replace(" ", "").lower()
     s=str(input("Enter a string:"))

     if( s == s[::-1] ):

      print("Word is palindrome")
     else:
      print("Word is not palindrome")
is_palindrome('s')