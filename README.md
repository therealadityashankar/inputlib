# inputlib
handle python inputs with ease!

## usage

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
