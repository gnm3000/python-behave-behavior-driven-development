from behave import Given, When, Then
from main import incrementor
@Given("a new incrementor of size {stride}")
def given_incrementor(context,stride:str):
    context.incrementor = incrementor(int(stride))
    
@When("we increment {num}")
def when_increment(context,num: str):
    context.result = context.incrementor(int(num))
    
@Then("we should see {results}")
def then_results(context,results:str):
    assert(context.result == int(results))
    