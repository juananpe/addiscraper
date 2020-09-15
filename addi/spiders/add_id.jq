def add_id(prefix):
  [ foreach .[] as $o (0;
      . + 1;
      $o + {"id": (prefix + tostring) }) ];

add_id("")
