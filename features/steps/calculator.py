from behave import Given, When, Then
from calc import Calculator

@Given("Calculator app is run")
def given_app(context):
    context.calc_method = Calculator.calc
    
@When("I input {eval_string} to calculator")
def when_input(context,eval_string):
    context.result = context.calc_method(eval_string)

    
@Then("I get the result {result_number}")
def then_result(context,result_number):
    
    assert(5 == int(result_number))