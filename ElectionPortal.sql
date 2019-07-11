CREATE TABLE user (
  user_id INT AUTO_INCREMENT NOT NULL ,
  username VARCHAR(20) NOT NULL,
  password VARCHAR(100) NOT NULL,
  isAdmin BOOL NOT NULL,
  PRIMARY KEY(user_id)
);

CREATE TABLE student(
  student_id INT NOT NULL,
  first_name VARCHAR(40) NOT NULL,
  last_name VARCHAR(40) NOT NULL,
  phone INT(10) NOT NULL,
  email VARCHAR(60) NOT NULL,
  PRIMARY key(student_id),
  FOREIGN KEY(student_id) REFERENCES user(user_id) ON DELETE CASCADE
);


create table faculty(
	faculty_id INT NOT NULL ,
	first_name varchar(40) NOT NULL,
	last_name varchar(40) NOT NULL,
	phone INT NOT NULL,
	email varchar(60) NOT NULL,
	PRIMARY KEY(faculty_id),
	Foreign key(faculty_id) references user(user_id) ON DELETE CASCADE
);


create table election(
	faculty_id INT NOT NULL,
	session_id INT AUTO_INCREMENT NOT NULL ,
	post varchar(20) NOT NULL,
	year INT(5) NOT NULL,
	status INT NOT NULL,
	PRIMARY KEY(session_id),
	Foreign KEY(faculty_id) references faculty(faculty_id) ON DELETE CASCADE
);

create table candidate(
	candidate_id INT AUTO_INCREMENT,
	user_id INT NOT NULL,
	session_id INT NOT NULL,
	PRIMARY KEY(candidate_id),
	Foreign key(session_id) references election(session_id) ON DELETE CASCADE
);

create table result(
	user_id INT NOT NULL,
	session_id INT NOT NULL,
	PRIMARY KEY(session_id),
	Foreign key(user_id) references user(user_id) ON DELETE CASCADE
);

create table vote(
	reference_no INT AUTO_INCREMENT,
	session_id INT NOT NULL,
	hashed_value VARCHAR(100) NOT NULL,
	candidate_id INT,
	PRIMARY key(reference_no),
	Foreign key(session_id) references election(session_id) ON DELETE CASCADE
);


