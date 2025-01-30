from dataclasses import dataclass,asdict
import rich
import json

@dataclass
class Config:
    ##----------------- General parameters -----------------##
    seed: int
    rvs_size: int

    ##----------------- Class Functions -----------------##
    def print(self):
        rich.print(f"cfg = {self}")

    def to_json(self):
        return json.dumps(asdict(self),sort_keys=True,indent=2)

    @classmethod
    def from_json(cls,json_str):
        return cls(**json.loads(json_str))
