# My decisions - Fuzzing implementation
### **Preface**
Before doing any programming or research, i got familiar with the code provided and started to comment it, mainly the main function in **fuzzer.py**. I also downloaded any neccessary libraries and downloaded the manual for JSON. 

### **Research**
When deciding on how to approach this task, I initially had to do some research on how JSON worked, what datatypes that were valid and how the libraries worked. I also did some research on different approaches to generate random data, since thats what fuzzing is all about. My main focus when researching was on **Unicode** characters. Other than that, i did some research on how to generate large integers and floats aswell as small integers and small floats but also how nested JSON objects worked. I came to the conclusion to use the build in **sys** library for generating large and small numbers.

### **Implementation**
When my resarch was done and i knew what to do the path was straight forward. I implemented a total of 14 functions that generates random data to fuzz. For instance, one function generates random strings, another generates random integers and so on. I also implemented a function that generates a random JSON object. This function uses the other functions to generate random data, like the string generator or integer generator. 

The function that took the longest time to implement was the function that generates random unicode strings. This was because i had to do some research on how unicode worked and how to generate random unicode strings based on **hexadecimal** intevals.

In the beginning my main focus was to generate very unique and random strings together with sequences of strings and integers/floats. But due to that implementation being pretty fast, my main focus was laid on the implementation of unicode strings.

Lastly, upon submission i stubbled upon a problem on on Linkedin where someone in a Python group asked for help with nested for-loops. This got me thinking about nesting in this assignment and lead me to implementing a nesting for the JSON objects. I implemented a nesting function that returns a list of nested JSON objects where you can define the amount of depth you want.

### **Conclusion**
Since fuzzing is all about testing the boundaries of a program based on completly random input, i think my implementation is good enough to test a vast majority of all cases. When running the code there is a few mismatches between the libraries. These mismatches are mainly due to encoding with unicode strings, mainly very long unicode strings. The libraries seem to encode pretty much the same for normal inputs, such as Ints, strings, floats and lists. Which is what to expect from an encoder. I really dont know why there is a large difference in encoding for the unicode strings, but the only thing i can think of is because of different encodings for the unicode itself, such as UTF-8. Not only might this be a translation problem but also in the sense that the bits might differ. This assignment has been quite challenging because i had to trie multiple things inorder to come out with something i belive is testing the functionallity properly. Also, i have learned that building software is challenging and that you will never be able to build a software that is 100% bug free, meaning fuzzing any software would most likely lead to you finding some bugs. I have gathered a skill that i will be able to apply in the future, and that is very nice.

### Libraries used(other than the given ones)
- **sys** - Used for generating large and small integers and floats.
- **random** - Used to be able to gather random data.
- **time** - Used for generating random seeds.

# References
- Unicode data: https://www.microfocus.com/documentation/silk-performer/195/en/silkperformer-195-webhelp-en/GUID-6AFC32B4-6D73-4FBA-AD36-E42261E2D77E.html 
- Valid JSON datatypes: https://www.w3schools.com/js/js_json_datatypes.asp
- Msgspec: https://github.com/jcrist/msgspec
- Orjson: https://github.com/ijl/orjson
- Json: https://docs.python.org/3/library/json.html