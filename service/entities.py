import typing as t
import typing_extensions as te

from pydantic import BaseModel, Field, ConstrainedInt, PositiveInt, PositiveFloat, ConstrainedFloat 



class windspeedFloat(ConstrainedFloat):
     ge = 0
     le = 0.85

class humInteger(ConstrainedFloat):
     ge = 0
     le = 1

    
class weathersitFloat(ConstrainedFloat):
     ge = 1
     le = 4

class seasonInteger(ConstrainedInt):
     ge = 1
     le = 4

class diffFloat(ConstrainedFloat):
     ge = -233.208
     le = 174.33

class atempFloat(ConstrainedFloat):
     ge = 0
     le = 1

class tempFloat(ConstrainedFloat):
     ge = 0.02
     le = 1
class yesterdayfloat(ConstrainedFloat):
     ge = 18.37
     le = 363.083
class holidayInteger(ConstrainedInt):
     ge = 0
     le = 1
class weekdayInteger(ConstrainedInt):
     ge = 0
     le = 6
class workingdayInteger(ConstrainedInt):
     ge = 0
     le = 1





class ModelInput(BaseModel):
    season:seasonInteger
    holiday: holidayInteger
    weekday: weekdayInteger
    workingday: workingdayInteger
    weathersit:weathersitFloat
    temp:tempFloat
    atemp:atempFloat
    hum:humInteger
    windspeed:windspeedFloat
    yesterday:yesterdayfloat
    diff:diffFloat
    

