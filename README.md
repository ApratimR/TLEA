# TLEA (Totally Logical Encryption Algorithm)

<img src="TLEA.png" width="400">

As the Acronym says its a Logical (Pun found?? ) , under-development symmetric key encryption algorithm that aim to 
* be secure
* be fast
* easy to modify
* able to avoid various attacks


Reason i am making this thing :
* i am just intrested in making/understanding this kind of stuff
* and this is also my university project

### Requirement

* made on ```numpy == 1.19.1```


### How to use

1. drop the file ```tlea.py``` in the directory of your file in which you want to use

2. use the script below as reference

```py
import tlea

thedata = "qwerty"
thekey = "test"


#mode 1 is for encryption
a = tlea.tlea(data=thedata,key=thekey,mode=1)
print(a)  #V3cgIW1eKnteMSgzQWlNSFJadTUzUVJtNzIgakZjXyYgSi4kfit0bycnTkh5fl9cKDRoemgldV5xdHxkKzpibFpbXiRgTFlHKXJ7SSVsJWhUX2QsLzhdNDZndEldI0g=


#mode 2 is decryption
a = tlea.tlea(a,thekey,2)
print(a)  #qwerty
```


## TODOs

- [X] make it work
- [ ] improve security (need to use chaining to avoid pattern based attack)


# WARNING

### Do not use it for production use as testing is till done