# Copyright 2022 InstaDeep Ltd. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

UNEXPLORED_ID: int = -1
IS_MINE: int = 1
PATCH_SIZE: int = 3
REVEALED_EMPTY_SQUARE_REWARD: float = 1.0
REVEALED_MINE_OR_INVALID_ACTION_REWARD: float = 0.0
COLOUR_MAPPING: list = [
    "orange",
    "blue",
    "green",
    "red",
    "purple",
    "maroon",
    "teal",
    "black",
    "gray",
]
