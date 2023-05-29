Feature: Upload text CV
    An UI element that allows job seeker upload CV as a text

    Scenario: Uploading text
        Given I'm a job seeker
        And I have text of the CV

        When I go to the main page
        And I paste text in the CV section
        And I press 'Upload' button

        Then I should not see the error message
        And the CV should be uploaded # to the DB