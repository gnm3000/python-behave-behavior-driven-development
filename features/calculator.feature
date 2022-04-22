Feature: Testing the Calculator
        Scenario: Addition
  # steps here
            Given Calculator app is run
             When I input 2+3 to calculator
             Then I get the result 5
