# RACE PACE

## By Mark Todman

![Launch page screenshot.](/assets/images/readme-images/race-pace-amiresponsive.png)

The deployed [Race Pace](https://race-pace-marktodman.herokuapp.com/) app.

The [GitHub repository.](https://github.com/marktodman/race-pace)

---
## OVERVIEW

1. [Race Pace Concept](#Race-Pace-Concept)
2. [Planning](#Planning)
3. [How to use Race Pace](#How-to-use-Race-Pace)
4. [Testing](#Testing)
5. [Deployment](#Deployment)
6. [Future Development Ideas](#Future-development-ideas)
7. [Credits](#Credits)

## RACE PACE CONCEPT

Race Pace is an online application for calculating finish times in popular running race distances: Marathon, Half Marathon, 10km and 5km. Race Pace allows the user to calculate either the pace required to reach a target race finish time, or their race finish time if they run at a user-specified average pace. 

Race Pace will also provide split information to help guide the runner through their race. The split information is times that the runner should be passing certain distance markers in their race. 

Race Pace will work in either kilometers or miles based on the user's preference.

### Target Audience:

- Runners who want to know how to pace their race to achieve a target finish time.
- Runners who want to know what their finish time will be if they run a particular pace in their race.
- Runners who want to improve their race times and race pacing.
- Coaches working with runners to improve their race times and race pacing.

## HOW TO USE RACE PACE

Users are guided through screens to generate the pacing information. Race Pace returns personalised information, so the first stage is for the user to input their first name.

The user selects their race distance: Marathon, Half Marathon, 10km, 5km. All calculations will be based on their selection.

The user selects their prefered units: kilometers or miles. All calculations will be based on their selection.

The user can then select whether they have a target finish time and would like to calculate the required pace to achieve the target. Or, whether they have a target pace and would like to know what finish time this would produce in their race.

Once this selection is made Race Pace calculates and returns the finish time and the pace, together with split times for given distance markers in the race.

## PLANNING

User stories were considered in the application design:

#### First Time User

> *"As an experienced runner, I would like to know how fast I should run to > achieve a target time at various race distances"*
>
> *"As a new runner, I would like to know what finish time I will achieve based on my current training pace"*
>
> *"As a coach, I would like to calculate paces and finish times to help guide my runners"*

#### Returning User

> *"As a returning user, I would like to be able to change the race pace or target time"*
>
> *"I would like to change the race distance as my experience grows"*
>
> *"I would like to be able to see my previous records"*

#### Developer

> *"As the app developer, I want to ensure a positive UX through defensive coding"*
> *"I want to guide the user through the app"*
> *"I want to produce accurate and meaningful output for the target audience"*

## FEATURES

The app is designed to guide the user through the necessary steps to calculate their race pace to acheive their race goals. As the app is hosted in a terminal display, this has been centred on the page. A background image of runners provides context to the app. The RACE PACE title text (named 'speed' on [figlet.org](http://www.figlet.org/fontdb_example.cgi?font=speed.flf)) is coloured in white and green to ephamise that the app is designed for race pacing.

![Screenshot of Race Pace start page.](assets/images/readme-images/race-pace-screenshot.png)

To personalise the UX, the first stage is for the user to input their first name. Only alpha characters are accepted and numbers or blanks will return an error.

![Example of numeric input error.](assets/images/readme-images/numeric-name-error.png)

The app provides feedback on each input so the user can see their input. This is especially useful in free text input. Text that the user has input is printed with blue text on a white background, The user has the chance to 'Restart' if they have made an error at any stage.

![Name input feedback.](assets/images/readme-images/name-input.png)

The app is menu driven to reduce user typograph error and enhance UX. Each menu contains users options which direct the user through a pathway to deliver a race pace, race time and race splits for their chosen distance. The menu options provide user choice and control, allowing defensive coding to protect the app and produce the desired output for the user. 'Exit' and 'Restart' options exist on each menu. 'Exit' closes the app. Once closed the user can restart by clicking the 'Start Race Button' which is always present onscreen. 'Restart' starts the app from the beginning, allowing the user to enter a new name and continuing through the menus from the start.

![The distance option menu.](assets/images/readme-images/distance-menu.png)

![The distance option menu user feedback.](assets/images/readme-images/distance-menu-user-feedback.png)

Only numbers 1 to 5 are accepted as valid input. Numbers outside of this range will generate an error message and the menu will reload. Alpha characters will also generate an error message and the menu will reload. This continues until the user inputs a number between 1 and 5. All error messages are printed in red text on a white background.

![Example error message for an incorrect number.](assets/images/readme-images/distance-menu-num-error.png)

![Example error message for a free text input.](assets/images/readme-images/distance-menu-alpha-error.png)

These error checks are coded into every menu selection. The user will not be allowed to advance until a valid input is made.

Once the user has selected their race distance, they are given a choice of whether they prefer to measure in kilometers or miles. This user selection is made once and then the chosen units are used for all calculations.

![The units menu options.](assets/images/readme-images/units-menu.png)

The user is then asked whether they have a target pace or target finish time for their race. This allows the user to chose to calculate the race splits and either finish time (based on pace) or necessary pace (based on target finish time).

![The targets menu options.](assets/images/readme-images/targets-menu.png)

At this point the user goes onto one their chosen path and are either asked to input their target race finish time or their target race pace.

![The target finish time input.](assets/images/readme-images/target-finish-time.png)

![The target pace input.](assets/images/readme-images/target-pace.png)

The inputs for both target finish time and target pace are free text. The input must be in the format specified in the text. For the finish time, this must be H:MM:SS. For shorter distances, likely to be completed in less than one hour (e.g. 5km) the hour units must still be input. For the pace input, both MM:SS and M:SS formats can be input. Inputs not in these formats, or that do not represent a recognised time format will generate error messages. The request for input will continue until a valid input is input by the user.

![Time input error message.](assets/images/readme-images/incorrect-time-input.png)

![Pace input error message.](assets/images/readme-images/incorrect-pace-input.png)

![Text input error message.](assets/images/readme-images/incorrect-pace-alpha-input.png)

Once the user has input either their target finish time or target pace, the app calculates either the race pace required to achieve the target finish time, or the finish time based on the target pace. 

The display presents the output of the race finish time, race pace and split times for certain distances markers in the race. Outputs are printed in green text on a white background.

![Output based on target finish time and km.](assets/images/readme-images/splits-km-target-time.png)

![Output based on target finish time and miles.](assets/images/readme-images/splits-miles-target-time.png)

![Output based on target pace time and km.](assets/images/readme-images/splits-km-target-pace.png)

The user is then asked whether they would like to calculate another race pace. The choice will either restart the process at the distance selection page, retaining the user name, or will exit the application.



