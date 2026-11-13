from hypothesis import given, strategies as st
import pytest
from irrigation_scheduler import parse_irrigation_schedule, calculate_total_water

@given(st.text() | st.none())
def test_parse_irrigation_schedule_fuzz(schedule_str):
    try:
        result = parse_irrigation_schedule(schedule_str)
        assert isinstance(result, list)
    except (ValueError, TypeError):
        pass  # Expected exceptions for malformed or invalid inputs

@given(
    st.lists(st.integers() | st.floats()) | st.none(),
    st.integers() | st.floats() | st.none()
)
def test_calculate_total_water_fuzz(durations, flow_rate):
    try:
        result = calculate_total_water(durations, flow_rate)
        assert isinstance(result, (int, float))
    except (ValueError, TypeError):
        pass  # Expected exceptions for invalid parameters