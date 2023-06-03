Feature: Upload text CV
    As a job seeker
    I want to upload my CV
    So that system can use this data to prepare cover letter

    Scenario: Uploading text CV
        Given I'm a job seeker
        And I have text of the CV

        When I go to the main page
        And I paste text in the CV section
        And I press 'Upload' button

        Then the CV should be uploaded # to the DB