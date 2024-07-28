DROP DATABASE keyloggerdb;

CREATE DATABASE keyloggerdb;
USE keyloggerdb;

CREATE TABLE logs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    key_log TEXT,
    screenshot LONGBLOB,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE USER 'goldfire'@'localhost' IDENTIFIED BY '123456';

GRANT ALL PRIVILEGES ON keyloggerdb.* TO 'goldfire'@'localhost';
    FLUSH PRIVILEGES;
