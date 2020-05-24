<?php
/**
 * @param \DateTime|null $value The value to format
 * @return string
 */
function format(DateTime $value) {
    return $value->format('y-m-d');
}
