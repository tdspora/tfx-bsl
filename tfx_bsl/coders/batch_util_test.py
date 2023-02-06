# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Tests for tfx_bsl.coders.batch_util."""

from tfx_bsl.coders import batch_util
from absl.testing import absltest


class BatchUtilTest(absltest.TestCase):

  def testGetBatchElementsKwargs(self):
    kwargs = batch_util.GetBatchElementsKwargs(batch_size=None)
    target_batch_duration_secs_including_fixed_cost = kwargs.pop(
        "target_batch_duration_secs_including_fixed_cost", None
    )
    self.assertIn(target_batch_duration_secs_including_fixed_cost, {1, None})
    self.assertDictEqual(
        kwargs,
        {
            "min_batch_size": 1,
            "max_batch_size": 1000,
            "target_batch_overhead": 0.05,
            "target_batch_duration_secs": 1,
            "variance": 0.25,
        },
    )
    kwargs = batch_util.GetBatchElementsKwargs(batch_size=5000)
    self.assertDictEqual(
        kwargs, {"max_batch_size": 5000, "min_batch_size": 5000}
    )


if __name__ == "__main__":
  absltest.main()
