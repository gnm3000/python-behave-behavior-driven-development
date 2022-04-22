Feature: Testing the incrementor
        Scenario: Testing increasing a number
            Given a new incrementor of size 5
             When we increment 10
             Then we should see 15

        Scenario: Testing decreasing a number
            Given a new incrementor of size -2
             When we increment 20
             Then we should see 18

        Scenario: Testing doing nothing to a number
            Given a new incrementor of size 0
             When we increment 15
             Then we should see 15
