# inputlib: handle python inputs with ease!
cause the `input()` command is not good enough!

## Intro :metal:

### installation

symbolic
```
pip3 install -a .
```

proper
```
pip3 install .
```


### a brief example

```
>>> import inputlib
>>>
>>> def foo():
...     print("bar :)")
...
>>>
>>> inp = inputlib.PInput()
>>> inp.add_keyword("foo", foo)
>>>
>>> inp.ask()
::>>> foo
bar :)
>>>
```

### another brief example
```
>>> inp = inputlib.PInput(")>")
>>> inp.add_keyword("foo")
>>> inp.add_keyword("bar")
>>>
>>> inp = inp.get_input()
>>> if input == "foo":
>>>     print("hey foo guy!")
>>> else input == "bar":
>>>     print("hey bar guy!")
```

### available tools

* class: `inputlib.PInput`
* def: `inputlib.get_conformation`

<br>

## Docs :v:

### class `inputlib.PInput`
creates a parsable input class

#### :sake: params:

**optional**

`foretext` - *string* - *default:* "::>>> " - the text that comes before what the user inputs
<br>

#### :sake: properties:

**:orange: `keywords`** - list of keywords

**:orange: `functions`** - dict of functions, args, and kwargs key is keyword name

**:orange: `foretext`** - text that comes before when the user inputs text

**:orange: `input_asked`** - was the input asked ? (using the ask() def)

**:orange: `retrieved_input`** - which input was called last

#### :sake: methods:

** :watermelon: `add_keyword`** - adds a usable keyword to the class

#### params:

##### **required**

`keyword` - *string* - adds a keyword to the class

##### **optional**

`keyword_callback` - *callable (function, class, if something else callable exists)* - function to be executed when the keyword is entered    
`callback_args` - *tuple* - callback function args

`callback_kwargs` - *dict* - callback function keyword args

<br>

**:watermelon: `ask`** - asks with an input

#### params: none

<br>

**watermelon: `get_input`** - gets user inputted keyword, raises an **PInputInputNotEnteredExeception** if user data has not been entered before this function was called.

#### params: none
<br>
### def `get_confirmation`
confirms *yes/no* with the user
#### :sake: params: none
