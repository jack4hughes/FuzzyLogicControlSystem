# Fuzzy Logic Controller

This is a basic fuzzy logic controller, implemented within python using a mix of functional and Object Oriented approaches

## Basic Idea:
A fuzzy logic controller is a type of control system that aims to be human readable, easy to implemeent, and able to deal with nonlinear problems.

Instead of a traditional control system, that relies on analytical functions to operate, a fuzzy logic controller relies on logical operations on "fuzzy sets." This allows it to deal with non-linear inputs and multiple inputs and outputs in an intuative way.

A fuzzy logic controller has 5 main steps:

``` Mermaid
    flowchart TD

    Input(input)
    Output(Output)
    Fuzzification
    InferenceEngine[Inference Engine]
    RuleSet[Rule Set]
    DeFuzification

    Input -->
    Fuzzification --> InferenceEngine
    RuleSet --> InferenceEngine -->
    DeFuzification -->
    Output
```
in this code, all these steps are handled within a FuzzyLoficController class. However, the functions used to fuzzify and defuzzify the data are constructed using a functional approach, allowing easy combinations of functions, and hopefully cleaner code.

## Fuzzification:
TODO: Write more here.

## Defuzzification:
TODO: Write more here.

## Inference Engine:
TODO: Write more here

## Ruleset
TODO: Write more here.

# Contact Details

for more information, contact me at jack4.hughes@live.uwe.ac.uk