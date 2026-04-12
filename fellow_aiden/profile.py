"""Model to validate the coffee profile data"""
from pydantic import BaseModel, field_validator, ValidationError
from typing import List
import re

RATIO_ENUM = [14 + 0.5 * i for i in range(13)]                   # 14, 14.5, 15, ... , 20
BLOOM_RATIO_ENUM = [1 + 0.5 * i for i in range(5)]               # 1, 1.5, 2, 2.5, 3
BLOOM_DURATION_ENUM = list(range(1, 121))                        # 1 to 120
OVERALL_TEMPERATURE_ENUM = [50 + 0.5 * i for i in range(99)]     # 50, 50.5, 51, 51.5 ... 99
BLOOM_TEMPERATURE_ENUM = [50 + 0.5 * i for i in range(99)]       # 50, 50.5, 51, 51.5 ... 99
PULSES_NUMBER_ENUM = list(range(1, 11))                          # 1 to 10
PULSES_INTERVAL_ENUM = list(range(5, 61))                        # 5 to 60
PULSE_TEMPERATURE_ENUM = [50 + 0.5 * i for i in range(99)]       # 50, 50.5, 51, 51.5 ... 99

# allows A–Z, a–z, 0–9, and the specials !@#$%&*-+?/.,:)(
TITLE_REGEX = re.compile(r'[A-Za-z0-9 !@#$%&*\-+?/.,:)(]+')

class CoffeeProfile(BaseModel):
    profileType: int
    title: str
    ratio: float
    overallTemperature: float
    bloomEnabled: bool
    bloomRatio: float
    bloomDuration: int
    bloomTemperature: float
    ssPulsesEnabled: bool
    ssPulsesNumber: int
    ssPulsesInterval: int
    ssPulseTemperatures: List[float]
    batchPulsesEnabled: bool
    batchPulsesNumber: int
    batchPulsesInterval: int
    batchPulseTemperatures: List[float]
    
    @field_validator('title')
    @classmethod
    def validate_title(cls, v):
        if len(v) > 50:
            raise ValueError(f"title must be less than or equal to 50 characters. Got {v}")
        if not TITLE_REGEX.fullmatch(v):
            raise ValueError(f"title only allows A–Z, a–z, 0–9, and the specials !@#$%&*-+?/.,:)(. Got {v}")
        return v
    
    @field_validator('ratio')
    @classmethod
    def validate_ratio(cls, v):
        if v not in RATIO_ENUM:
            raise ValueError(f"ratio must be one of {RATIO_ENUM}. Got {v}")
        return v

    @field_validator('overallTemperature')
    @classmethod
    def validate_overall_temperature(cls, v):
        if v not in OVERALL_TEMPERATURE_ENUM:
            raise ValueError(f"overallTemperature must be one of {OVERALL_TEMPERATURE_ENUM}. Got {v}")
        return v

    @field_validator('bloomRatio')
    @classmethod
    def validate_bloom_ratio(cls, v):
        if v not in BLOOM_RATIO_ENUM:
            raise ValueError(f"bloomRatio must be one of {BLOOM_RATIO_ENUM}. Got {v}")
        return v
    
    @field_validator('bloomDuration')
    @classmethod
    def validate_bloom_duration(cls, v):
        if v not in BLOOM_DURATION_ENUM:
            raise ValueError(f"bloomDuration must be one of {BLOOM_DURATION_ENUM}. Got {v}")
        return v
    
    @field_validator('bloomTemperature')
    @classmethod
    def validate_bloom_temperature(cls, v):
        if v not in BLOOM_TEMPERATURE_ENUM:
            raise ValueError(f"bloomTemperature must be one of {BLOOM_TEMPERATURE_ENUM}. Got {v}")
        return v
    
    @field_validator('ssPulsesNumber')
    @classmethod
    def validate_ss_pulses_number(cls, v):
        if v not in PULSES_NUMBER_ENUM:
            raise ValueError(f"ssPulsesNumber must be one of {PULSES_NUMBER_ENUM}. Got {v}")
        return v
    
    @field_validator('ssPulsesInterval')
    @classmethod
    def validate_ss_pulses_interval(cls, v):
        if v not in PULSES_INTERVAL_ENUM:
            raise ValueError(f"ssPulsesInterval must be one of {PULSES_INTERVAL_ENUM}. Got {v}")
        return v
    
    @field_validator('ssPulseTemperatures')
    @classmethod
    def validate_ss_pulse_temperature(cls, v):
        for t in v:
            if t not in PULSE_TEMPERATURE_ENUM:
                raise ValueError(f"Each ssPulseTemperature must be one of {PULSE_TEMPERATURE_ENUM}. Got: {t}")
        return v
    
    @field_validator('batchPulsesNumber')
    @classmethod
    def validate_batch_pulses_number(cls, v):
        if v not in PULSES_NUMBER_ENUM:
            raise ValueError(f"batchPulsesNumber must be one of {PULSES_NUMBER_ENUM}. Got {v}")
        return v
    
    @field_validator('batchPulsesInterval')
    @classmethod
    def validate_batch_pulses_interval(cls, v):
        if v not in PULSES_INTERVAL_ENUM:
            raise ValueError(f"batchPulsesInterval must be one of {PULSES_INTERVAL_ENUM}. Got {v}")
        return v
    
    @field_validator('batchPulseTemperatures')
    @classmethod
    def validate_batch_pulse_temperature(cls, v):
        for t in v:
            if t not in PULSE_TEMPERATURE_ENUM:
                raise ValueError(f"Each batchPulseTemperature must be one of {PULSE_TEMPERATURE_ENUM}. Got: {t}")
        return v
    
