# inputlib: handle python inputs with ease!

## intro

### brief example

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

### available tools

* class: `inputlib.PInput`
* def: `inputlib.getConformation`

## Docs

### class `inputlib.PInput`

#### params:

##### optional
* **foretext** - *default:* "::>>> " - the text that comes before what the user inputs

#### class methods:
* **add_keyword** - adds a usable keyword to the class

  * params:

    * required:
      * **keyword** - *string* - adds a keyword to the class
      * **keyword_callback** - *callable (function, class, if something else callable exists)* - function to be executed when the keyword is entered
      * **callback_args** - *tuple* - callback function args
      * **callback_kwargs** - *dict* - callback function keyword args


