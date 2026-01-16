""" Constants used by other files """

DOMAIN = "room_light_control"
DOMAIN_SHORT = "rlc"

#-> Input Variables
CONF_TARGETS = "targets"
CONF_ROOM = "room"
CONF_ROOMS = "rooms"

CONF_MOTION_SENSOR = "motion_sensor"
CONF_MOTION_SENSORS = "motion_sensors"
CONF_MOTION_SENSOR_RESETS_TIMER = "motion_sensor_resets_timer"

CONF_TURN_OFF_SENSOR = "turn_off_sensor"

CONF_ILLUMINANCE_SENSOR = "illuminance_sensor"
CONF_ILLUMINANCE_SENSOR_THRESHOLD = "illuminance_sensor_threshold"
DEFAULT_ILLUMINANCE_THRESHOLD = 5.0

DEFAULT_DELAY = 180

# activate_light_script_or_scene (either script or scene)
ACTIVATE_LIGHT_SCRIPT_OR_SCENE = "activate_light_script_or_scene"
# turn_off_light (script)
CONF_TURN_OFF_LIGHT = "turn_off_light"
# timeout
CONF_TURN_OFF_DELAY = "turn_off_delay"

CONF_TURN_OFF_BLOCKING_ENTITY = "turn_off_blocking_entity"
CONF_TURN_OFF_BLOCKING_ENTITIES = "turn_off_blocking_entities"

CONF_LUX_MIN = "lux_min"
CONF_LUX_MAX = "lux_max"
CONF_BRIGHTNESS_MIN = "brightness_min"
CONF_BRIGHTNESS_MAX = "brightness_max"

CONF_HOME_STATUS_ENTITY = "home_status_entity"
CONF_HOME_STATUS_BEHAVIORS = "home_status_behaviors"

CONF_ADAPTIVE_DIMMING = "adaptive_dimming"
CONF_ADAPTIVE_DIMMING_INTERVAL = "adaptive_dimming_interval"
CONF_ADAPTIVE_DIMMING_MIN_DELTA = "adaptive_dimming_min_delta"
CONF_ADAPTIVE_DIMMING_COOLDOWN = "adaptive_dimming_cooldown"
CONF_ADAPTIVE_DIMMING_TARGET_LUX = "adaptive_dimming_target_lux"
CONF_ADAPTIVE_DIMMING_GAIN = "adaptive_dimming_gain"
CONF_ADAPTIVE_DIMMING_DEADBAND = "adaptive_dimming_deadband"
CONF_ADAPTIVE_DIMMING_MAX_STEP = "adaptive_dimming_max_step"

STATES = ['idle', 'blocked',
          {'name': 'active', 'children': ['control'],
           'initial': False}]
CONF_IGNORE_STATE_CHANGES_UNTIL = "grace_period"


CONTEXT_ID_CHARACTER_LIMIT = 26
