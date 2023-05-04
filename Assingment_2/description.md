# My decisions - Fuzzing implementation
### Research
When deciding on how to approach this task, I initially had to do some research on how JSON worked, what datatypes that were valid and how the libraries worked. I also did some research on different approaches to generate random data, since thats what fuzzing is all about. My main focus when researching was on **Unicode** characters. Other than that, i did some research on how to generate large integers and floats aswell as small integers and small floats.

### Implementation
When my resarch was done and i knew what to do the path was straight forward. I implemented a total of 14 functions that generates random data to fuzz. For instance, one function generates random strings, another generates random integers and so on. I also implemented a function that generates a random JSON object. This function uses the other functions to generate random data, like the string generator or integer generator. 

The function that took the longest time to implement was the function that generates random unicode strings. This was because i had to do some research on how unicode worked and how to generate random unicode strings based on **hexadecimal** intevals.

### Conclusion
Since fuzzing is all about testing the boundaries of a program based on completly random input, i think my implementation is good enough to test a vast majority of all cases. When running the code there is a few mismatches between the libraries. These mismatches are mainly due to encoding with large numbers but also for very long and unique unicode sequences.


# References
- Unicode data: https://www.microfocus.com/documentation/silk-performer/195/en/silkperformer-195-webhelp-en/GUID-6AFC32B4-6D73-4FBA-AD36-E42261E2D77E.html 
- Valid JSON datatypes: https://www.w3schools.com/js/js_json_datatypes.asp
- Msgspec: https://github.com/jcrist/msgspec
- Orjson: https://github.com/ijl/orjson
- Json: https://docs.python.org/3/library/json.html